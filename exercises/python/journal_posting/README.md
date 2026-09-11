# Journal posting

**Language:** Python · **AI:** off · **Time:** ~45 minutes · **Starter:** `ledger.py`

## Background

A general ledger records every economic event as a **journal**: a memo plus two or more
**lines**. Each line names an account and moves money in one direction, as a debit or a
credit. Within a single journal, total debits must equal total credits. This is the rule
that makes the whole system self-checking. If a journal breaks it, the ledger is wrong,
and every report built on the ledger (trial balance, P&L, balance sheet) is wrong too.

A cash sale of $100 looks like this:

| Account | Debit | Credit |
| --- | ---: | ---: |
| `cash` | 10000 | 0 |
| `revenue` | 0 | 10000 |

Amounts are integer **cents** everywhere. There are no floats in this exercise, and there
should not be any in your solution.

## Your task

Implement `Ledger.post_journal` in `ledger.py`. It should either store a valid journal
and return it, or raise `PostingError` and leave the ledger unchanged.

```python
def post_journal(self, lines: list[JournalLine], memo: str = "") -> Journal:
```

The surrounding types are already written for you:

- `JournalLine(account_id: str, debit_cents: int, credit_cents: int)` is a frozen dataclass.
- `Journal(id: str, lines: tuple[JournalLine, ...], memo: str)`.
- `PostingError(ValueError)` is what to raise for anything you reject.
- `Ledger.journals()` is already implemented. It returns a copy of what has been posted.
- `Ledger._next_id` is a counter you may use to mint journal ids. Any scheme works as long
  as the id is non-empty and unique.

### Rules the tests enforce

1. **Balanced journals post.** The sum of `debit_cents` across lines equals the sum of
   `credit_cents`. On success, return the stored `Journal` with a non-empty `id`, and
   `ledger.journals()` grows by one.
2. **Unbalanced journals are rejected.** Raise `PostingError` and post nothing. A
   rejected journal must not appear in `journals()`, even partially.
3. **Empty journals are rejected.** A journal with no lines has no meaning.
4. **A single line cannot be both a debit and a credit.** `JournalLine("cash", 5000, 5000)`
   is not a zero-effect line. It is a modelling error. It also keeps the journal
   "balanced", which is why it needs its own check.

## Running the tests

```bash
cd exercises/python/journal_posting
pytest -q
```

All four tests fail with `NotImplementedError` until you write the method. Start by
reading `test_ledger.py`. It is the spec.

## What we care about

The balance check should live in the posting path and fail hard. It should not live in a
comment, a docstring, or the caller. We want to see how you name and structure the
validation, what error information a caller gets back, and whether the ledger is really
unchanged after a rejection. Talk through your reasoning as you go. How you decide what to
check matters more to us than how fast you type.

## Where the conversation usually goes

Once the tests pass, we will usually talk through some of these. You do not need to
implement them unless we ask:

- The same Stripe charge arrives twice and posts two identical journals. How do you make
  posting idempotent?
- A controller wants to fix a typo in the memo of a journal posted last month.
- Someone posts to a parent/header account that exists only to group other accounts.
- The period the journal belongs to has already been closed.
- Two processes post with the same idempotency key at the same instant.

## Constraints

Please use integer cents throughout, never floats. Do not rebalance a journal by
inserting a plug line to make it fit, and do not leave validation to the UI. This
exercise is run without AI assistance. Language documentation is fine.
