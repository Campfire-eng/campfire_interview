# Python exercises

Four self-contained exercises. Each folder has a starter module, a test file that acts as
the specification, and a README that explains the accounting problem and the contract you
are implementing. Nothing depends on anything outside its own folder.

| Folder | Exercise | AI |
| --- | --- | --- |
| [`journal_posting/`](journal_posting/) | Post a journal that cannot unbalance the books | Off |
| [`bank_matching/`](bank_matching/) | Propose matches between bank lines and GL cash lines | Off for a screen, on otherwise |
| [`prepaid_amortization/`](prepaid_amortization/) | Straight-line prepaid schedule in whole cents | On |
| [`categorization_eval/`](categorization_eval/) | Evaluate a GL-coding model in dollars, not just counts | On |

## Setup

Python 3.10 or newer, and `pytest`. There are no other dependencies.

```bash
pip install pytest
```

## Running

`conftest.py` and `pytest.ini` put each exercise folder on the import path, so both of
these work:

```bash
cd coding/python
pytest -q                        # everything
pytest journal_posting -q        # one exercise

cd coding/python/journal_posting
pytest -q                        # also fine
```

Every suite starts red with `NotImplementedError`. That is intentional. The failing test
tells you what the function is supposed to do.

## Before you start

Read the exercise README first, then the test file, then the starter module. Money is
integer cents in all four exercises. If something in the spec is unclear, ask. Deciding
what to clarify is part of the exercise.
