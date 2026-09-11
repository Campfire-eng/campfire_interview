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
