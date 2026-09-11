from datetime import date

from amortize import monthly_straight_line


def test_twelve_equal_months():
    posts = monthly_straight_line(120_000, date(2026, 1, 1), 12)
    assert len(posts) == 12
    assert sum(p.expense_cents for p in posts) == 120_000
    assert posts[-1].prepaid_remaining_cents == 0
    assert posts[0].expense_cents == 10_000


def test_remainder_goes_to_last_month():
    posts = monthly_straight_line(100, date(2026, 1, 1), 3)
    assert [p.expense_cents for p in posts] == [33, 33, 34]
    assert sum(p.expense_cents for p in posts) == 100


def test_rejects_bad_inputs():
    for kwargs in (
        {"total_cents": 0, "start": date(2026, 1, 1), "months": 12},
        {"total_cents": 100, "start": date(2026, 1, 1), "months": 0},
    ):
        try:
            monthly_straight_line(**kwargs)
        except ValueError:
            continue
        raise AssertionError("expected ValueError")
