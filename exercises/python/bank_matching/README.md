# Bank matching

**Language:** Python · **AI:** off when used as a screen, on for onsite or take-home · **Time:** ~50 minutes, or ~3 hours as a take-home · **Starter:** `matching.py`

## Background

Bank reconciliation is the process of proving that what the bank says happened matches
what the books say happened. Every month a controller stares at two lists:

- **Bank transactions** — what actually moved through the account, straight from the feed.
- **GL cash lines** — what the company recorded against its cash account.

Most lines pair up one-to-one. The interesting ones do not:

- A **batch deposit**: the bank shows one $300 credit; the GL shows three separate $100
  customer payments that the bank swept together.
- A **split payment**: the GL shows one $500 bill; the bank shows two withdrawals.
- **Timing**: a payment recorded in the GL on the 9th clears the bank on the 11th.
- **Coincidence**: two different customers each paid $50 on the same day, and only one of
  them corresponds to the bank line you are looking at.

This is a constrained assignment problem with an audit requirement bolted on. The output
is not a decision — it is a *proposal* a human will accept or reject, so every proposal
has to carry an explanation the controller can evaluate in a couple of seconds.

## Your task

Implement `propose_matches` in `matching.py`.

```python
def propose_matches(
    bank: list[BankTxn],
    gl: list[GLLine],
    date_window_days: int = 3,
) -> list[MatchProposal]:
```

The types are already defined:

- `BankTxn(id, amount_cents, booked_on, reference="")` — `amount_cents` is **signed**;
  deposits are positive, withdrawals negative.
- `GLLine(id, amount_cents, effective_on, reference="")` — same signing convention, on the
  cash account.
- `MatchProposal(bank_ids: tuple[str, ...], gl_ids: tuple[str, ...], confidence: float, reason: str)`.

`bank_ids` and `gl_ids` are tuples so a single proposal can express one-to-one, one-to-many,
and many-to-one relationships in the same shape.

### Rules the tests enforce

1. **One-to-one exact match.** Equal amounts within `date_window_days` of each other pair
   up. A GL line dated the 11th can match a bank line booked on the 10th.
2. **No line is consumed twice.** Every bank id and every GL id may appear in **at most one**
   proposal across the whole returned list. If two $50 bank transactions compete for a
   single $50 GL line, exactly one proposal comes back and the other bank line is left
   unmatched. Leaving something unmatched is a correct answer; double-spending a GL line
   is not.
3. **One bank transaction, many GL lines.** A $300 deposit on the 10th matches a $100 line
   on the 9th plus a $200 line on the 10th, because the amounts sum and both fall inside
   the window. This comes back as a single proposal with two `gl_ids`.

`confidence` and `reason` are not asserted by the tests, but they are part of the
deliverable — a proposal a controller cannot interpret is not usable.

## Running the tests

```bash
cd exercises/python/bank_matching
pytest -q
```

Three tests, all failing on `NotImplementedError` to start.

## What we care about

Signals worth using: amount (the strongest by far), the date window, and `reference` as a
weak corroborating hint. Ordering should be deterministic — the same inputs must produce
the same proposals in the same order, because a reconciliation that reshuffles itself
between runs is not auditable. Think about how you keep the search for summing subsets from
exploding as the candidate lists grow, and be explicit about the tradeoff you chose.

This is deliberately not a string-distance puzzle. Matching primarily on vendor or memo
text is the wrong shape for the problem.

## Where the conversation usually goes

- There is a $2.50 wire fee on the bank side that never made it into the GL. Do you match
  with a tolerance, and who gets to set that tolerance?
- A $10,000 deposit is 40 individual checks. How does your approach behave?
- Two customers paid the identical amount on the same day.
- A human overrides one of your proposals. What happens to the others that depended on
  those lines being free?
- How would you measure whether this is any good — against what data, using what metric?

## Constraints

Every proposal needs a human-readable `reason`. No GL line may appear in two proposals.
If we are running this as a screen, work without AI assistance; for onsite or take-home,
use whatever tools you like, but you own everything you submit.
