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

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Trains on auto-approved predictions with no human labels and no awareness of the feedback loop. One global model keyed on raw account ids across tenants. Nothing records which model version produced a posted entry. Fine-tuning is offered as the answer to every quality problem. |
| 2 | Suggestions and outcomes are logged, a training table is built, retraining runs on a schedule, and a test set is held out. Point-in-time correctness of features, tenancy of models, and label delay during close are missing or vague until asked. Shadow mode and output validation against the tenant's chart of accounts come up only when prompted. |
| 3 | Features are point-in-time correct, or a feature store is proposed. Per-tenant versus shared models are separated with a clear view of what generalizes, such as vendor semantics, versus what does not, such as account ids. Label delay during close, class imbalance, shadow mode before auto-post, and structured output validated against the tenant's real chart are covered. The follow-ups on tenant opt-out, training on its own outputs, and a one-customer fix are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: training-serving skew, leakage when corrected labels reappear as features, and privacy and contractual limits on cross-tenant training with a way to still benefit from shared learning. Per-customer calibration, rollback when a new model regresses one entity, and cost and latency budgets at hundreds of thousands of transactions a month are covered. The audit story for which model version coded a given transaction is explicit, with tradeoffs stated. |
