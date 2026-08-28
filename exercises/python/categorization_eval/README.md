# Q17 — Categorization model evaluation (Python, AI-on)

```bash
cd exercises/python
pytest categorization_eval -q
```

The tests are deliberately shaped so count accuracy looks fine (2 of 3 auto-approved
correct) while the single wrong item is $5,000 of the $5,130 auto-approved. Once the
suite is green, ask the real question: **where do you set the threshold, and what do
you tell the controller it costs them?**

Senior follow-ups: label noise (ground truth is a human correction), contaminated
holdouts, drift after a chart of accounts change, calibration, and per-entity slicing.
