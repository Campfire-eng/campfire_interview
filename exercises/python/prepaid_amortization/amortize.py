from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class AmortizationPost:
    period_start: date
    expense_cents: int
    prepaid_remaining_cents: int


def monthly_straight_line(
    total_cents: int,
    start: date,
    months: int,
) -> list[AmortizationPost]:
    """Equal monthly expense; remainder cents land in the final month.

    `start` is the first day of the first period (interviewers may later
    ask for mid-month conventions).
    """
    raise NotImplementedError
