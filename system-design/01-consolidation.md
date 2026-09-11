# Multi-entity consolidation

| | |
| --- | --- |
| Time | 45 min |
| Format | Whiteboard or shared document |
| AI | Off |
| Usually for | Backend, platform |

## The prompt

A customer has 60 subsidiaries in 25 countries. Each subsidiary keeps its own books in
its own currency. The parent company reports in USD. Subsidiaries sell to each other, and
ownership of some subsidiaries is less than 100%. Today the finance team produces a
consolidated income statement and balance sheet once a month by exporting each
subsidiary's trial balance into a spreadsheet. It takes three days.

Design a system that produces consolidated statements on demand, with the ability to
drill from any consolidated figure down to the underlying entries in a subsidiary.

## Background

Consolidation means combining the financial statements of a group of companies as if they
were one company. Three things make it more than adding up the numbers:

- **Translation.** Each subsidiary's amounts are in its own currency and have to be
  converted to the reporting currency. Different kinds of accounts use different rates,
  and the difference that results is recorded in a specific equity account.
- **Elimination.** When one subsidiary sells to another, both the sale and the purchase
  are real in the subsidiaries' books but do not exist from the group's point of view. They
  have to be removed in the consolidated view without changing the subsidiaries' books.
- **Ownership.** If the parent owns 80% of a subsidiary, the consolidated statements
  include 100% of that subsidiary's results and show the other 20% separately as
  non-controlling interest.

Each subsidiary also closes its own books on its own schedule, and a consolidated
statement is only final when every subsidiary in it is closed.

## What we ask you to produce

- A data model covering entities, ownership, the per-entity ledgers, exchange rates, and
  the consolidated result.
- The flow from a posted entry in a subsidiary to a figure in a consolidated statement.
- How intercompany transactions are identified and eliminated.
- How drill-down works from a consolidated figure to the source entries.
- What happens when an exchange rate is corrected after a statement has been produced.

## Follow-ups

- "Subsidiary A billed subsidiary B $50,000 and B has not recorded it yet."
- "The parent sold 30% of a subsidiary on the 12th of the month."
- "Two subsidiaries have a fiscal year ending in March; the rest end in December."
- "The controller wants to see last month's consolidated revenue exactly as it was
  reported to the board, even though a subsidiary has posted late entries since."

## Rubric

| Area | Strong | Weak |
| --- | --- | --- |
| Requirements | Asks about ownership changes, fiscal year differences, and whether the consolidated view needs to be final or can be provisional. Decides early whether to compute on demand or materialize. | Treats it as a reporting query over all entities. Does not ask about ownership or currency. |
| Data model | Per-entity ledgers stay separate and untouched. Ownership is a timeline, not a single percentage. Rates are keyed by date and source. Eliminations and translation adjustments live in a separate consolidation layer with their own entries. | One combined ledger for all entities. A single ownership percentage per entity. One global exchange rate. |
| Correctness | Names the invariants: subsidiary books are never modified by consolidation, the consolidated balance sheet still balances after translation, eliminations net to zero, and non-controlling interest is shown for partial ownership. Shows where each is checked. | Adds up the entities and stops. Eliminates by deleting or hiding subsidiary transactions. No translation adjustment, so the consolidated balance sheet does not balance. |
| Controls and audit | Each consolidation run is recorded with its inputs: which entity periods, which rate set, which ownership table. A run can be reproduced. Provisional and final runs are distinguished. | Consolidated figures are computed live with no record of what went into them. No way to tell if an entity was still open when the figure was produced. |
| Failure handling | A corrected exchange rate produces a new run and a visible difference, not a silent change. Late entries in a subsidiary are handled by re-running and comparing. Intercompany mismatches are surfaced as exceptions, not forced to balance. | Rate corrections overwrite prior results. Intercompany mismatches are plugged to make the numbers match. |
| Communication | Draws the layers clearly: entity ledgers, translation, elimination, consolidated result. Explains the tradeoff between computing on demand and storing results. Adjusts the design when the ownership follow-up arrives. | Hard to see where translation and elimination happen. Cannot explain how a figure could be traced back. |
