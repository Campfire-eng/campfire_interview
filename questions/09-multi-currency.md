# 9. Multi-currency: functional versus reporting

| | |
| --- | --- |
| Track | System design |
| Language | Verbal |
| Format | Design |
| AI | **Off** |
| Time | 45 min |

**The problem.** The entity operates in EUR, the parent reports in USD, vendors bill in
GBP, and Stripe settles in USD. Design how amounts, rates, revaluation, and statements
work.

**Why we ask it.** An amount in a multi-currency ledger is a measured quantity plus an
explicit translation. It is never a single number.

**What a strong answer covers.** Storing the original currency and amount, a rate table
keyed by date, converting for reporting. Then: a functional currency per entity, monetary
versus non-monetary items, period-end revaluation producing unrealized FX journals,
realized FX on settlement, and spot versus average rates for the balance sheet versus the
P&L understood as policy backed by a standard rather than a preference. Beyond that:
cumulative translation adjustment on consolidation, a single rate source of truth, rates
frozen for closed periods, and explaining an FX movement by citing rate identifiers
instead of describing it in words.

**Follow-ups.** "March is closed and on April 2 the rate feed restates March 31." "We hold
cash in a currency that isn't the entity's functional currency."

**Common problems.** One `amount_usd` column and nothing else. Revaluing equity the
same way as cash.
