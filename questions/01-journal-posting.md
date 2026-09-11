# 1. Post a journal that cannot unbalance the books

| | |
| --- | --- |
| Track | Backend |
| Language | Python |
| Format | Pair |
| AI | **Off** |
| Time | 45 min |
| Starter | `coding/python/journal_posting` |

**The problem.** Implement `post_journal(lines) -> Journal`. Each line has `account_id`,
`debit_cents`, and `credit_cents` as non-negative integers. Reject anything that would
violate double-entry. Storage is in-memory.

**Why we ask it.** Every journal has to balance. The rest of the product depends on that.
We want to see you check it in code and return an error when it fails, instead of leaving
it to a comment or to the caller.

**What a strong answer covers.** The sum of debits equals the sum of credits. Empty
journals are rejected. A line that is somehow both a debit and a credit is rejected.
All-zero lines are rejected. Error types are clear and tell a caller what was wrong.
Beyond that: an idempotency key so the same event cannot post twice, a check that the
period is open, a check that the account exists and is postable rather than a header used
for grouping, and posted journals treated as immutable, so you reverse rather than edit.
If you get that far, we will talk about money as integer cents throughout, your rounding
policy, how multi-currency lines would land later, emitting an event after commit without
losing it, and what happens when two posters race the same idempotency key.

**Follow-ups.** "A controller posted to a parent account." "They want to fix a memo typo
after posting." "The same Stripe charge arrives twice."

**Common problems.** Using floats for money. Adding a line to make an unbalanced journal
balance. Editing posted lines instead of reversing them. Expecting the UI to validate the
input.
