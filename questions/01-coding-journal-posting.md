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

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | The journal can be posted unbalanced, or the balance check exists but can be bypassed. Money is stored as floats. Errors are generic or silent. The candidate adds a balancing line to make a bad journal fit, or edits posted lines in place. |
| 2 | Balanced journals are enforced and unbalanced ones are rejected with an error. Empty journals, all-zero lines, and lines with both a debit and a credit may slip through. Errors do not say what was wrong. No thought given to duplicates, periods, or immutability until asked. |
| 3 | All of the basic invariants are enforced with clear error types. The candidate raises at least one of idempotency, period status, or postable accounts on their own, and handles the rest well when asked. Posted journals are treated as immutable, with reversal as the correction path. |
| 4 | Everything in 3, plus the candidate gets to the deeper material unprompted: an idempotency key with a defined race behavior, a period check, header versus postable accounts, and a stated rounding policy. They can say how multi-currency lines and post-commit events would fit without changing the core. Code is clean and tested. |
