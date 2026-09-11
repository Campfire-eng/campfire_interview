# 15. Duplicate detection across integrations

| | |
| --- | --- |
| Track | Data engineering + backend |
| Language | Python |
| Format | Pair |
| AI | **On** |
| Time | 45 min |

**The problem.** The same spend can arrive from a card integration, the bank feed, and a
manual journal. Detect probable duplicates before they hit posted books. False positives
annoy controllers; false negatives fail the audit.

**Why we ask it.** This is a question about identity and provenance. It is not mainly
about fuzzy string matching.

**What a strong answer covers.** Exact match on amount, date, and vendor as a baseline.
Then: provenance keys per source; distinguishing "this bank line settles that card charge"
from "this is a second booking of the same spend"; windowed blocking to keep comparisons
bounded; a resolution queue; and never auto-voiding a posted journal. Further: modelling
the same economic event across sources as a graph, intercompany transfers that look like
duplicates, refunds and reversals, weighing reviewer time against missed duplicates,
idempotent detectors that can be safely re-run, and how the feature explains itself in the
UI.

**Follow-ups.** "Two employees, same restaurant, same amount, same day." "A card refund
arrives three weeks later."

**Common problems.** A global unique constraint on (amount, date). Silently dropping
one feed.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | A global unique constraint on (amount, date), or fuzzy string matching as the whole design. One feed is silently dropped, or a posted journal is auto-voided. No distinction between a settlement and a second booking of the same spend. |
| 2 | Exact match on amount, date, and vendor as a baseline. Provenance keys per source and the settlement-versus-duplicate distinction only surface when asked. Comparison cost and what happens to a flagged pair are not thought through. |
| 3 | Provenance keys per source, and a clear separation between a bank line settling a card charge and a second booking of the same spend. Windowed blocking keeps comparisons bounded, flagged pairs go to a resolution queue, and posted journals are never auto-voided. The two-employees and late-refund follow-ups are handled well. |
| 4 | Everything in 3, plus the further material unprompted: the same economic event modelled as a graph across sources, intercompany transfers that look like duplicates, refunds and reversals, reviewer time weighed against missed duplicates, idempotent detectors that can be safely re-run, and how the feature explains itself in the UI. Tradeoffs are stated. |
