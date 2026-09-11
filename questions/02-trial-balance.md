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
