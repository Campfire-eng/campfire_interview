# Prepaid amortization

**Language:** Python · **AI:** allowed · **Time:** ~45 minutes · **Starter:** `amortize.py`

## Background

When a company pays for something up front that it will use over time, such as a year of
insurance, an annual software licence, or a prepaid retainer, it cannot expense the whole
payment on the day the cash leaves. Paying $120,000 on January 1 for twelve months of
insurance buys an asset: the right to twelve months of coverage. Each month, one month
of that right is used up, so $10,000 moves from the prepaid asset to insurance expense
and the remaining asset balance drops.

That monthly movement is **amortization**, and the list of future movements is the
**schedule**. Two properties matter most:

- The schedule must sum exactly to what was paid. Approximately is not enough. A rounding
  remainder of three cents left on the balance sheet is a reconciling item somebody has
  to chase down at year end.
- The remaining balance must reach exactly zero in the final period.

$100 over 3 months does not divide evenly. The convention here is equal amounts each
period, with the remainder going into the last one: `33, 33, 34`.

## Your task

Implement `monthly_straight_line` in `amortize.py`.

```python
def monthly_straight_line(
    total_cents: int,
    start: date,
    months: int,
) -> list[AmortizationPost]:
```

Return one `AmortizationPost(period_start, expense_cents, prepaid_remaining_cents)` per
month, in chronological order.

- `total_cents` is the full prepaid amount, in integer cents.
- `start` is the first day of the first period. (Mid-month start dates are a follow-up
  discussion, not part of the tests.)
- `months` is how many periods the amount spreads across.

### Rules the tests enforce

1. **Even division.** `monthly_straight_line(120_000, date(2026, 1, 1), 12)` returns 12
   posts, each with `expense_cents == 10_000`, summing to `120_000`, with the final post's
   `prepaid_remaining_cents == 0`.
2. **Remainder lands in the last month.** `monthly_straight_line(100, date(2026, 1, 1), 3)`
   returns expenses of exactly `[33, 33, 34]`.
3. **Bad inputs raise `ValueError`.** A `total_cents` of `0` and a `months` of `0` are both
   rejected.

`period_start` should be the first day of each successive month, and
`prepaid_remaining_cents` is what is left on the asset after that period's expense.

## Running the tests

```bash
cd coding/python/prepaid_amortization
pytest -q
```

## What we care about

Money stays in integer cents. Rolling a `date` forward by a month is easy to get slightly
wrong, so pick an approach you can explain. Most of all, the sum-to-total and end-at-zero
properties should hold because of how the code is built, not by accident. If a reviewer
has to run the numbers to be convinced, the code is not clear enough.

AI assistance is allowed on this exercise. We will read the result together. We are as
interested in what you noticed and corrected as in what the model generated.

## Where the conversation usually goes

- The policy starts on January 17 instead of the 1st. Daily convention or a stub period?
- They cancel on June 1 and get a partial refund. What happens to the remaining schedule
  and to the already-posted entries?
- The month you are about to post into has been closed. You cannot edit a locked period.
  Where does the expense go?
- The month-end job runs twice. Does anything double up?
- Where does the prepaid rollforward report come from: the schedule, or the posted
  journals?

## Constraints

No floats for money. Do not amortize into a closed period by rewriting old journals. A
posted journal is a historical record, and corrections happen through new entries.
