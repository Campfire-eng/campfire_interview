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
