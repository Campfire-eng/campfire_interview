"""In-memory ledger. Candidate fills this in. Money is integer cents."""

from __future__ import annotations

from dataclasses import dataclass, field


class PostingError(ValueError):
    pass


@dataclass(frozen=True)
class JournalLine:
    account_id: str
    debit_cents: int
    credit_cents: int


@dataclass
class Journal:
    id: str
    lines: tuple[JournalLine, ...]
    memo: str


@dataclass
class Ledger:
    _journals: list[Journal] = field(default_factory=list)
    _next_id: int = 1

    def post_journal(self, lines: list[JournalLine], memo: str = "") -> Journal:
        raise NotImplementedError

    def journals(self) -> list[Journal]:
        return list(self._journals)
