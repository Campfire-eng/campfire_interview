"""Evaluate GL account suggestions. Candidate implements `evaluate`.

Predictions above `auto_approve_threshold` post without human review, so errors
in that population are the ones that reach the books.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Prediction:
    txn_id: str
    amount_cents: int
    predicted_account: str
    confidence: float


@dataclass(frozen=True)
class Label:
    txn_id: str
    actual_account: str


@dataclass(frozen=True)
class AccountMetrics:
    precision: float
    recall: float


@dataclass(frozen=True)
class EvalReport:
    coverage: float
    auto_approved_count: int
    reviewed_count: int
    auto_approved_accuracy: float
    auto_approved_error_cents: int
    per_account: dict[str, AccountMetrics]


def evaluate(
    predictions: list[Prediction],
    labels: list[Label],
    auto_approve_threshold: float,
) -> EvalReport:
    """Precision and recall span all predictions; the auto-approved metrics
    cover only predictions at or above the threshold.
    """
    raise NotImplementedError
