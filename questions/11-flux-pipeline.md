# 11. Flux analysis pipeline

| | |
| --- | --- |
| Track | Data engineering |
| Language | Python |
| Format | Pair or take-home |
| AI | **On** |
| Time | 50 min, or 3 hours as a take-home |

**The problem.** A nightly job computes, per account and optionally per department,
current period versus prior period versus prior year, in dollars and percent, flagging
material movements. Controllers then ask Ember why travel went up.

**Why we ask it.** The hard part is definitions, grain, and explainability. It is not a
question about Spark.

**What a strong answer covers.** Grouping by period and account, joining the prior period,
avoiding divide-by-zero. Then: materiality expressed as both an absolute and a percentage,
direction interpreted according to account type, late postings handled through as-of
snapshots, the flux run persisted so a downstream answer cites a frozen number, and
dimension support. Deeper: statistical versus judgmental flagging, new and renumbered
accounts, comparability after an acquisition, FX-neutral flux, incremental computation
over millions of lines, stopping the run when the trial balance does not balance, and
grounding commentary in the top contributing vendors and journals.

**Follow-ups.** "The period is not closed yet. Do we still publish flux?" "Account 6100 was
split into 6100 and 6101 this year."

**Common problems.** Percent change as the only signal. Ad-hoc recomputation with no
run id. Ignoring account-type direction, so a revenue increase is flagged as a problem.
