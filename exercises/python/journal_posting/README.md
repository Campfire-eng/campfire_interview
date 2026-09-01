# Journal posting

**Language:** Python · **AI:** off · **Time:** ~45 minutes · **Starter:** `ledger.py`

## Background

A general ledger records every economic event as a **journal**: a memo plus two or more
**lines**. Each line names an account and moves money in one direction — a *debit* or a
*credit*. The rule that makes the whole system self-checking is that within a single
journal, total debits must equal total credits. A journal that violates this is not a
slightly-wrong journal; it is a corrupt ledger, and every report built on top of it —
trial balance, P&L, balance sheet — silently becomes wrong.

A cash sale of $100 looks like this:

| Account | Debit | Credit |
| --- | ---: | ---: |
| `cash` | 10000 | 0 |
| `revenue` | 0 | 10000 |

Amounts are integer **cents** everywhere. There are no floats in this exercise, and there
should not be any in your solution.

## Your task

Implement `Ledger.post_journal` in `ledger.py` so that it either stores a valid journal
and returns it, or raises `PostingError` and leaves the ledger untouched.

```python
def post_journal(self, lines: list[JournalLine], memo: str = "") -> Journal:
```

The surrounding types are already written for you:

- `JournalLine(account_id: str, debit_cents: int, credit_cents: int)` — frozen dataclass.
- `Journal(id: str, lines: tuple[JournalLine, ...], memo: str)`.
- `PostingError(ValueError)` — raise this for anything you reject.
- `Ledger.journals()` — already implemented; returns a copy of what has been posted.
- `Ledger._next_id` — a counter you may use to mint journal ids. Any scheme works as long
  as the id is non-empty and unique.

### Rules the tests enforce

1. **Balanced journals post.** Sum of `debit_cents` across lines equals sum of
   `credit_cents`. On success, return the stored `Journal` with a non-empty `id`, and
   `ledger.journals()` grows by one.
2. **Unbalanced journals are rejected.** Raise `PostingError`, and post *nothing* — a
   rejected journal must not appear in `journals()` even partially.
3. **Empty journals are rejected.** A journal with no lines is meaningless.
4. **A single line cannot be both a debit and a credit.** `JournalLine("cash", 5000, 5000)`
   is not a zero-effect line, it is a modelling error, and it happens to keep the journal
   "balanced" — which is exactly why it needs an explicit check.

## Running the tests

```bash
cd exercises/python/journal_posting
pytest -q
```

All four tests fail with `NotImplementedError` until you write the method. Start by
reading `test_ledger.py`; it is the spec.

## What we care about

The invariant should live in the posting path as a hard failure, not in a comment or a
docstring or the caller. We are interested in how you name and structure the validation,
what error information a caller gets back, and whether the ledger is genuinely unchanged
after a rejection. Talk through your reasoning as you go — how you decide what to check
is more interesting to us than how fast you type it.

## Where the conversation usually goes

Once the tests are green, expect to discuss some of these out loud. You do not need to
implement them unless we ask:

- The same Stripe charge arrives twice and posts two identical journals. How do you make
  posting idempotent?
- A controller wants to fix a typo in the memo of a journal posted last month.
- Someone posts to a parent/header account that exists only to group other accounts.
- The period the journal belongs to has already been closed.
- Two processes post with the same idempotency key at the same instant.

## Constraints

Please use integer cents throughout, never floats. Do not "helpfully" rebalance a journal
by inserting a plug line to make it fit, and do not treat validation as something the UI
will handle. This exercise is run without AI assistance — language documentation is fine.
