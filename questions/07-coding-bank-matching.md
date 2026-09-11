# 7. Score bank transactions against GL candidates

| | |
| --- | --- |
| Track | Data engineering + backend |
| Language | Python |
| Format | Pair or take-home |
| AI | **On** for onsite or take-home; **off** if used as a screen |
| Time | 50 min, or 3 hours as a take-home |
| Starter | `coding/python/bank_matching` |

**The problem.** Given unmatched bank transactions and unmatched GL cash lines, produce
match proposals: one-to-one, one-to-many (a batch deposit), and many-to-one (a split
payment). Score them and explain them. Use amount, date window, reference, and
counterparty. String distance alone is not enough here.

**Why we ask it.** Matching is a constrained assignment problem with an audit requirement
attached. The explanation is part of the deliverable, not an extra.

**What a strong answer covers.** Exact amounts inside an N-day window, leftovers left
unmatched, tests. Then: one-to-many where amounts sum, no line consumed twice, confidence
scores, deterministic tie-breaking, reference and memo used as weak signals, currency
awareness. The hard parts are controlling combinatorial explosion, treating fee and FX
differences as a tolerance policy rather than a fixed constant, partial matches that
need a residual journal, human override always winning, an evaluation set that measures
precision and recall against historical reconciliations, and why embeddings are a last
resort here.

**Follow-ups.** "There's a $2.50 bank fee not in the GL." "A $10,000 deposit is 40 checks."
"Two customers paid the same amount on the same day."

**Common problems.** Matching on vendor name alone. Allowing one GL line into two
proposals. No explanation string for the controller.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Matching is done on vendor name or string distance alone. One GL line can appear in more than one proposal. Proposals carry no explanation string for the controller. Leftovers get forced into a match instead of being left unmatched. |
| 2 | Exact amounts are matched inside an N-day window, leftovers are left unmatched, and there are tests. One-to-many and many-to-one are missing or can consume a line twice. Confidence scores and explanations are thin, and tie-breaking is not deterministic. The bank fee, the batch deposit, and the same-amount collision are handled only when we raise them. |
| 3 | One-to-many and many-to-one work, amounts sum correctly, and no line is consumed twice. Each proposal has a confidence score and an explanation, ties break deterministically, and reference and memo act as weak signals with currency awareness. The $2.50 fee, the 40-check deposit, and two customers paying the same amount on the same day are handled well when asked. |
| 4 | Everything in 3, plus the candidate raises the hard parts on their own: bounding combinatorial explosion, fee and FX differences as a tolerance policy rather than a fixed constant, a residual journal for partial matches, and human override always winning. They propose an evaluation set that measures precision and recall against historical reconciliations, and can say why embeddings are a last resort here. Tradeoffs are stated. |
