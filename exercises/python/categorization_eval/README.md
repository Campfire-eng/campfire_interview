# Categorization model evaluation

**Language:** Python · **AI:** allowed · **Time:** ~50 minutes, or ~3 hours as a take-home · **Starter:** `eval.py`

## Background

A model looks at each incoming transaction and proposes which GL account it belongs to —
`travel`, `meals`, `software`, and so on — with a confidence score. Anything at or above an
**auto-approve threshold** posts straight to the books with no human involvement.
Everything below it goes into a review queue for a controller.

That threshold is the entire product decision. Set it high and you have built a slightly
faster spreadsheet, because humans still review everything. Set it low and wrong numbers
land in the general ledger unseen and end up in a board pack.

The trap in this exercise is that ordinary ML metrics do not describe the risk. In the
fixture data, three of four predictions clear a 0.90 threshold and two of those three are
correct — 67% accuracy on the auto-approved population, which sounds survivable. But the
single wrong one is a **$5,000** transaction, and the other two are $100 and $30 combined.
Nearly all of the dollars that posted without review posted wrong. Counting mistakes and
weighing mistakes give you opposite readings of the same model.

## Your task

Implement `evaluate` in `eval.py`.

```python
def evaluate(
    predictions: list[Prediction],
    labels: list[Label],
    auto_approve_threshold: float,
) -> EvalReport:
```

Inputs:

- `Prediction(txn_id, amount_cents, predicted_account, confidence)`
- `Label(txn_id, actual_account)` — ground truth, in practice a human's correction.

Return an `EvalReport` with:

| Field | Meaning |
| --- | --- |
| `coverage` | Fraction of all predictions that were auto-approved. |
| `auto_approved_count` | Predictions with `confidence >= auto_approve_threshold`. |
| `reviewed_count` | Predictions below the threshold. |
| `auto_approved_accuracy` | Share of auto-approved predictions whose account was right. |
| `auto_approved_error_cents` | Total `amount_cents` of auto-approved predictions that were **wrong**. |
| `per_account` | `dict[str, AccountMetrics]` of precision and recall. |

The population split matters: **precision and recall span all predictions**, while the
four auto-approve fields describe **only** the at-or-above-threshold population.

Precision for an account is (predictions of that account that were correct) / (all
predictions of that account). Recall is (predictions of that account that were correct) /
(all transactions whose true account was that one).

### Rules the tests enforce

Using the fixture in `test_eval.py` at a 0.90 threshold: `auto_approved_count == 3`,
`reviewed_count == 1`, `coverage == 0.75`, `auto_approved_accuracy == 2/3`, and
`auto_approved_error_cents == 500_000`. Per account, `travel` is 0.5 precision / 1.0
recall, `meals` is 1.0 / 0.5, `software` is 1.0 / 1.0.

Raising the threshold to 0.99 shrinks auto-approval to a single prediction, which happens
to be correct — accuracy 1.0 and error of 0 cents, bought with much lower coverage.

A prediction with no matching label raises `ValueError`. Silently scoring against a
partial label set is how an evaluation ends up flattering a model.

## Running the tests

```bash
cd exercises/python
pytest categorization_eval -q
```

## What we care about

Getting the arithmetic right is the first half. The second half is the conversation the
numbers are supposed to support: **where do you set the threshold, and what do you tell
the controller it costs them?** Have an answer that refers to review capacity and to
materiality, not just to a curve.

Watch the divide-by-zero cases — an account that appears in the labels but was never
predicted, or vice versa.

AI assistance is allowed. Metric code is exactly the kind of thing a model will write
confidently and subtly wrong, so read it like you are reviewing a colleague's pull request.

## Where the conversation usually goes

- Accuracy is 97% and the controller is furious. What happened?
- Labels only exist for items a human reviewed — and you stopped showing them the
  confident ones. What does that do to next quarter's evaluation?
- A customer renumbers their chart of accounts mid-year.
- Does 0.95 confidence actually mean 95%, and how would you find out?
- Same model, same overall numbers, but one entity is much worse than the others. Would
  this report show that?

## Constraints

A single accuracy number is not an evaluation. Any metric that ignores transaction amount
is describing a different business than this one.
