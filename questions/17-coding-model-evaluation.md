# 17. Evaluate the categorization model like an accountant

| | |
| --- | --- |
| Track | AI engineering + data engineering |
| Language | Python |
| Format | Pair or take-home |
| AI | **On** |
| Time | 50 min |
| Starter | `coding/python/categorization_eval` |

**The problem.** The model proposes GL accounts with a confidence score, and anything above
the auto-approve threshold posts without human review. Build the evaluation: coverage,
accuracy on auto-approved items, dollar-weighted error, and per-account precision and
recall. Then tell us where to set the threshold.

**Why we ask it.** An AI feature has to be evaluated in the units the business is exposed
to. Accuracy is the wrong headline metric, because one wrong $500k line matters more than
a hundred correct $12 ones.

**What a strong answer covers.** Correct precision, recall, and coverage, with no
divide-by-zero on unseen classes. Then: separating the auto-approved population from the
reviewed one, treating dollar-weighted error as the primary metric, framing threshold
selection as a trade between reviewer hours and misstatement risk, using a held-out
set that is not contaminated by items the model already had corrected, and breaking results
out per account because one bad account can be material on its own. The strongest answers
get into label quality (the ground truth here is a controller's correction, which is
itself noisy and delayed), drift monitoring after a chart of accounts change, slicing by
entity and vendor and new-vendor status, calibration so that 0.95 confidence really means
95%, connecting the eval to a rollout gate and a kill switch, and expressing tolerance in
accounting terms rather than F1 alone.

**Follow-ups.** "Accuracy is 97% and the controller is upset. What happened?" "We only
get labels on items humans reviewed, and we stopped showing them the confident ones." "A
customer renumbers their chart of accounts."

**Common problems.** A single accuracy number. Evaluating on training data. No notion
of amount anywhere. Choosing a threshold without reference to review capacity or
materiality.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Reports a single accuracy number, or metrics that divide by zero on unseen classes. Evaluates on training data or on items the model already had corrected. Amount does not appear anywhere in the evaluation. The threshold is picked without reference to review capacity or materiality. |
| 2 | Precision, recall, and coverage are computed correctly, with unseen classes handled. Auto-approved and reviewed items are lumped together, and dollar-weighted error is missing or secondary until asked. Threshold selection is a number without a stated trade. The held-out set and per-account breakout come up only when prompted. |
| 3 | Auto-approved and reviewed populations are evaluated separately, and dollar-weighted error is the primary metric. The threshold is framed as a trade between reviewer hours and misstatement risk, measured on a held-out set not contaminated by corrected items. Results are broken out per account. The follow-ups on label bias and a renumbered chart of accounts are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: noisy and delayed controller labels as ground truth, drift monitoring after a chart of accounts change, slicing by entity, vendor, and new-vendor status, and calibration so that 0.95 confidence really means 95%. The eval is tied to a rollout gate and a kill switch, and tolerance is stated in accounting terms rather than F1 alone. Tradeoffs between review load and misstatement risk are explicit. |
