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
