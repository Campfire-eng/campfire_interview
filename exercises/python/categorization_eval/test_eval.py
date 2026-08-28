from eval import Label, Prediction, evaluate

PREDICTIONS = [
    Prediction("t1", 10_000, "travel", 0.99),
    Prediction("t2", 500_000, "travel", 0.95),
    Prediction("t3", 2_000, "meals", 0.40),
    Prediction("t4", 3_000, "software", 0.98),
]

LABELS = [
    Label("t1", "travel"),
    Label("t2", "meals"),
    Label("t3", "meals"),
    Label("t4", "software"),
]


def test_coverage_and_populations():
    report = evaluate(PREDICTIONS, LABELS, auto_approve_threshold=0.90)
    assert report.auto_approved_count == 3
    assert report.reviewed_count == 1
    assert report.coverage == 0.75


def test_dollar_error_dominates_count_accuracy():
    report = evaluate(PREDICTIONS, LABELS, auto_approve_threshold=0.90)
    assert abs(report.auto_approved_accuracy - 2 / 3) < 1e-9
    # t2 is the only wrong auto-approved item, and it is the material one.
    assert report.auto_approved_error_cents == 500_000


def test_per_account_precision_and_recall():
    report = evaluate(PREDICTIONS, LABELS, auto_approve_threshold=0.90)
    travel = report.per_account["travel"]
    assert travel.precision == 0.5
    assert travel.recall == 1.0

    meals = report.per_account["meals"]
    assert meals.precision == 1.0
    assert meals.recall == 0.5

    software = report.per_account["software"]
    assert software.precision == 1.0
    assert software.recall == 1.0


def test_raising_threshold_trades_coverage_for_safety():
    report = evaluate(PREDICTIONS, LABELS, auto_approve_threshold=0.99)
    assert report.auto_approved_count == 1
    assert report.auto_approved_accuracy == 1.0
    assert report.auto_approved_error_cents == 0


def test_prediction_without_label_is_rejected():
    try:
        evaluate([Prediction("t9", 100, "travel", 0.99)], LABELS, 0.9)
    except ValueError:
        return
    raise AssertionError("expected ValueError for unlabeled prediction")
