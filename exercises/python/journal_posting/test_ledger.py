from ledger import JournalLine, Ledger, PostingError


def test_balanced_journal_posts():
    ledger = Ledger()
    journal = ledger.post_journal(
        [
            JournalLine("cash", 10_000, 0),
            JournalLine("revenue", 0, 10_000),
        ],
        memo="cash sale",
    )
    assert journal.id
    assert len(ledger.journals()) == 1


def test_unbalanced_journal_rejected():
    ledger = Ledger()
    try:
        ledger.post_journal(
            [
                JournalLine("cash", 10_000, 0),
                JournalLine("revenue", 0, 9_000),
            ]
        )
    except PostingError:
        assert ledger.journals() == []
        return
    raise AssertionError("expected PostingError")


def test_empty_journal_rejected():
    ledger = Ledger()
    try:
        ledger.post_journal([])
    except PostingError:
        return
    raise AssertionError("expected PostingError")


def test_line_cannot_be_both_debit_and_credit():
    ledger = Ledger()
    try:
        ledger.post_journal(
            [
                JournalLine("cash", 5_000, 5_000),
                JournalLine("revenue", 0, 0),
            ]
        )
    except PostingError:
        return
    raise AssertionError("expected PostingError")
