# 4. Multi-entity consolidation without the spreadsheet

| | |
| --- | --- |
| Track | System design |
| Language | Verbal (API shapes in either language if you want) |
| Format | Design |
| AI | **Off** |
| Time | 50 min |

**The problem.** Customers consolidate 5–200 subsidiaries across 180+ currencies, with
ownership changes and intercompany payables. They want a consolidated P&L in near real
time instead of a three-day Excel pack. Design the system.

**Why we ask it.** Consolidation is where a second source of truth often gets created
without anyone deciding to create it. It is also where elimination and ownership either
get modelled or get skipped over.

**What a strong answer covers.** Per-entity ledgers, translation into a reporting currency,
and a consolidation run. That is the frame. The substance is intercompany matching with
elimination entries booked in a consolidation layer rather than by deleting subsidiary
transactions, cumulative translation adjustment at least named, minority interest when
ownership is under 100%, per-entity close status versus group status, and an idempotent
recast when rates change. Pushing further: continuous versus batch consolidation,
materialization versus query-time, an ownership timeline for step acquisitions, differing
fiscal year-ends, overlay books, drilling from a consolidated figure back to entity-level
journals, and what the system does when one entity's period is still open.

**Follow-ups.** "Sub A billed Sub B $50k." "We sold 30% of a sub on the 12th." "The
controller wants to drill from consolidated revenue to Stripe invoices."

**Common problems.** Adding up all the entities and stopping there. Eliminating by deleting
transactions. One global FX rate with no date dimension.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | The design adds up the entities and stops there. Intercompany balances are eliminated by deleting subsidiary transactions, or not at all. There is one global FX rate with no date dimension. Ownership under 100% is not modelled. |
| 2 | Per-entity ledgers, translation into a reporting currency, and a consolidation run are described. Intercompany elimination, cumulative translation adjustment, minority interest, and per-entity versus group close status are missing or vague until asked. Rate changes have no defined recast behavior. |
| 3 | Intercompany matching produces elimination entries in a consolidation layer and subsidiary transactions are left alone. Cumulative translation adjustment is named, minority interest is handled when ownership is under 100%, and entity close status is separate from group status. A rate change triggers an idempotent recast. The intercompany billing, partial sale, and drill-to-Stripe follow-ups are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: continuous versus batch consolidation, materialization versus query-time, and an ownership timeline that handles step acquisitions. Differing fiscal year-ends, overlay books, drilling from a consolidated figure to entity-level journals, and what happens when one entity's period is still open are all addressed. Tradeoffs are stated. |
