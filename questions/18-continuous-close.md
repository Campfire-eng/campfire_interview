# 18. Continuous close and autonomous reconciliation

| | |
| --- | --- |
| Track | System design |
| Language | Verbal |
| Format | Design |
| AI | **Off** |
| Time | 50 min |

**The problem.** The pitch is that reconciliations happen continuously and payments match
invoices automatically, with control retained. Design the pipeline from bank, card, and
Stripe events through proposed journals, posted books, and certified reconciliations, for
a lean finance team.

**Why we ask it.** The question we care about is how control is preserved as automation
increases, not whether automation is possible.

**What a strong answer covers.** Event in, suggestion out, human posts, reconciliation
follows. Then: proposals as a distinct state from posted entries, thresholds, queues
ordered by risk, periods still governing everything, exactly-once posting, and
observability on lag and unmatched aging. The deeper version names what must never be
autonomous (locking, material estimates, related-party items) and covers backpressure,
model and policy version stamped on every auto-post, replaying a day of events, a reason
code and kill switch behind each automated action, and how certification stays meaningful
when a machine did the matching.

**Follow-ups.** "Model quality drops after a chart of accounts redesign." "Unmatched aging
hits ten days right before close."

**Common problems.** Auto-posting with no human visibility. No unmatched aging metric. A
close checklist that ignores what the automation did.
