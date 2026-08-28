from datetime import date

from matching import BankTxn, GLLine, propose_matches


def test_one_to_one_exact():
    bank = [BankTxn("b1", 10_000, date(2026, 3, 10), "ACH 99")]
    gl = [GLLine("g1", 10_000, date(2026, 3, 11), "ACH 99")]
    matches = propose_matches(bank, gl)
    assert len(matches) == 1
    assert matches[0].bank_ids == ("b1",)
    assert matches[0].gl_ids == ("g1",)


def test_does_not_reuse_gl_line():
    bank = [
        BankTxn("b1", 5_000, date(2026, 3, 10)),
        BankTxn("b2", 5_000, date(2026, 3, 10)),
    ]
    gl = [GLLine("g1", 5_000, date(2026, 3, 10))]
    matches = propose_matches(bank, gl)
    used = [gid for m in matches for gid in m.gl_ids]
    assert len(used) == len(set(used))
    assert len(matches) == 1


def test_batch_deposit_one_bank_many_gl():
    bank = [BankTxn("b1", 30_000, date(2026, 3, 10))]
    gl = [
        GLLine("g1", 10_000, date(2026, 3, 9)),
        GLLine("g2", 20_000, date(2026, 3, 10)),
    ]
    matches = propose_matches(bank, gl)
    assert len(matches) == 1
    assert set(matches[0].gl_ids) == {"g1", "g2"}
