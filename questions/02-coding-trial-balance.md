# 2. Trial balance and a P&L from the same lines

| | |
| --- | --- |
| Track | Backend, product-adjacent |
| Language | TypeScript |
| Format | Pair |
| AI | **Off** |
| Time | 45 min |
| Starter | `coding/typescript/trial_balance` |

**The problem.** Given accounts (`id`, `name`, `type`) and posted lines, return a trial
balance as of a date and an income statement for a period. Types are
`asset | liability | equity | revenue | expense`.

**Why we ask it.** Normal balances and statement construction are the layer that Ember
reports on. If the engine underneath is wrong, Ember will report wrong numbers.

**What a strong answer covers.** Netting each account correctly, producing balanced trial
balance columns, and computing the P&L as revenue minus expense over a window. The main
content is the difference between an as-of date and a period window, net income rolling
to equity, contra accounts, and handling closing entries on purpose rather than by
accident. Further in: retained earnings and the close process, cash versus accrual (this
data is accrual), drilling from a statement row down to the contributing journal ids, and
why you cannot produce a P&L by filtering a trial balance.

**Follow-ups.** "Add gross margin with a `cogs` subtype." "Give me the December P&L, but
the books contain a January reversing accrual."

**Common problems.** Treating every positive amount as a debit. Letting balance sheet
accounts appear in the P&L. Mixing up `posted_at` and `effective_date` without asking
which one the question means.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Positive amounts are treated as debits regardless of account type, so balances net wrong. Balance sheet accounts appear in the P&L, or the trial balance columns do not tie. The as-of date and the period window are treated as the same thing. posted_at and effective_date are used interchangeably without asking which one the question means. |
| 2 | Accounts net by normal balance and the trial balance columns tie. The P&L is revenue minus expense over a window and only includes revenue and expense accounts. The difference between an as-of date and a period window is present but shaky. Net income rolling to equity, contra accounts, and closing entries only come up when asked. |
| 3 | As-of versus period is handled cleanly and net income rolls to equity so the trial balance still ties. Contra accounts net correctly and closing entries are handled on purpose rather than by accident. The candidate asks which date field the question means. The cogs subtype and the January reversing accrual follow-ups are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: retained earnings and the close process, why this data is accrual rather than cash, and drilling from a statement row to the contributing journal ids. The candidate can explain why a P&L cannot be produced by filtering a trial balance. Code is clean and tested. |
