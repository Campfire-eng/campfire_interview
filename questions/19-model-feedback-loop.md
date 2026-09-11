# 19. The feedback loop that trains the accounting model

| | |
| --- | --- |
| Track | AI engineering + data engineering |
| Language | Python |
| Format | Design, optional pipeline sketch |
| AI | **On** |
| Time | 50 min |

**The problem.** Every controller correction is training signal. Design the pipeline that
turns accepted and rejected suggestions into features and labels, retrains or fine-tunes,
and ships safely, across customers with different charts of accounts and without leaking
one tenant's data into another's model.

**Why we ask it.** We want to see production ML thinking on top of a system of record:
data contracts, tenancy, and safe rollout. Framework names are not the point.

**What a strong answer covers.** Logging suggestions and outcomes, building a training
table, retraining on a schedule, holding out a test set. Then: a feature store, or at
minimum point-in-time-correct features so training never uses facts that were unavailable
at prediction time; per-tenant versus shared models and a clear view of what generalizes
(vendor semantics) versus what does not (account ids); label delay during close; class
imbalance; shadow mode before enabling auto-post; and structured output validated against
the tenant's real chart of accounts so the model cannot emit an account that does not
exist. Deeper: training-serving skew; leakage when corrected labels reappear as features;
privacy and contractual limits on cross-tenant training, and how customer data stays
protected while still benefiting from shared learning; per-customer calibration; rollback
when a new model regresses one entity; cost and latency budgets at hundreds of thousands
of transactions a month; and the audit story for which model version coded a given
transaction.

**Follow-ups.** "A customer demands their data never trains a shared model." "The model was
retrained on its own auto-approved outputs for three months." "Ship a fix for one customer
today without retraining everything."

**Common problems.** Training on auto-approved predictions with no human labels and no
awareness of the feedback loop. One global model keyed on raw account ids. No versioning of
what produced a posted entry. Fine-tuning offered as the answer to every quality problem.
