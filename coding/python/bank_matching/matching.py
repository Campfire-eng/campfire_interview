from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class BankTxn:
    id: str
    amount_cents: int  # signed: deposits positive, withdrawals negative
    booked_on: date
    reference: str = ""


@dataclass(frozen=True)
class GLLine:
    id: str
    amount_cents: int  # signed, cash account
    effective_on: date
    reference: str = ""


@dataclass(frozen=True)
class MatchProposal:
    bank_ids: tuple[str, ...]
    gl_ids: tuple[str, ...]
    confidence: float
    reason: str


def propose_matches(
    bank: list[BankTxn],
    gl: list[GLLine],
    date_window_days: int = 3,
) -> list[MatchProposal]:
    """Each bank id and gl id may appear in at most one proposal."""
    raise NotImplementedError
