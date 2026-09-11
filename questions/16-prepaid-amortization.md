# 16. Prepaid amortization engine

| | |
| --- | --- |
| Track | Backend engineering |
| Language | Python (TypeScript acceptable) |
| Format | Pair or take-home |
| AI | **On** |
| Time | 45 min |
| Starter | `coding/python/prepaid_amortization` |

**The problem.** $120,000 of annual insurance paid on January 1, amortized monthly.
Generate the prepaid asset, the monthly expense journals, and handle a mid-month start and
an early termination.

**Why we ask it.** We want to see how you handle schedules versus posted reality, stub
periods, and money that is never stored as a float.

**What a strong answer covers.** Twelve equal postings with the prepaid balance reaching
zero. Then: daily versus monthly convention, remainder cents landing deterministically,
refusing to post into a locked period so the expense accrues into the next open one, and a
month-end job that is idempotent. Beyond that: many schedules per vendor, termination and
impairment, FX on the original bill, linkage back to the source bill, and deriving the
prepaid rollforward from posted journals rather than a sidecar table that will drift.

**Follow-ups.** "Start date is January 17." "They cancel June 1 with a partial refund."

**Common problems.** Dividing dollars as floats. Amortizing into a locked period by
mutating old journals.
