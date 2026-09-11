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

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Amounts are stored in a single amount_usd column with no original currency or rate. Equity is revalued the same way as cash. Statements are produced by converting whatever is on hand at whatever rate is current. Functional and reporting currency are not distinguished. |
| 2 | The original currency and amount are stored, a rate table is keyed by date, and conversion for reporting is described. A functional currency per entity and monetary versus non-monetary items come up only when asked. Revaluation, realized versus unrealized FX, and spot versus average rates are handled thinly, and the restated March 31 rate is not addressed until we raise it. |
| 3 | Functional currency per entity is explicit, monetary and non-monetary items are treated differently, and period-end revaluation produces unrealized FX journals with realized FX on settlement. Spot versus average rates for the balance sheet versus the P&L is explained as policy backed by a standard rather than a preference. The restated March 31 rate and cash held in a non-functional currency are handled well. |
| 4 | Everything in 3, plus the candidate reaches the deeper material unprompted: cumulative translation adjustment on consolidation, a single rate source of truth, and rates frozen for closed periods. They explain an FX movement by citing rate identifiers instead of describing it in words. Tradeoffs are stated. |
