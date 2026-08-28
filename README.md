# Campfire interview kit

Accounting-domain screens for an AI-native ERP: general ledger, close, revenue recognition, reconciliation, integrations, and grounded AI over the books.

Campfire hires on **Python** and **TypeScript (Next.js / React)**. These exercises stay in that world. None of them are LeetCode.

## What's in here

| Path | Purpose |
| --- | --- |
| [interview-kit.md](interview-kit.md) | All **20 questions**: prompts, AI policy, junior / senior / staff bars, follow-ups, red flags |
| [loop.md](loop.md) | Screen and onsite mixes, including a track-specific table |
| [exercises/](exercises/) | Six starter repos with failing tests, for pairing or take-homes |

## Tracks

System design, schema design, product engineering, backend engineering, data engineering, and AI engineering, plus the controls work an ERP forces on you: permissions, segregation of duties, and auditability.

## AI policy

- **AI-off** means no Copilot, no chat assistant, no autocomplete writing logic. Language docs are fine and the candidate narrates as they go. These reveal whether they actually own double-entry, invariants, and edge cases.
- **AI-on** means tools are allowed. Grade product sense, review quality, and whether they catch the accounting bugs a model will happily ship.

A senior who is fast with AI and sloppy on debits and credits fails. A junior who is slow but protects the ledger can still clear the junior bar.

## Hands-on exercises

Every starter ships failing tests so the candidate begins by reading the spec.

```bash
cd exercises/python && pytest -q            # Q1, Q7, Q16, Q17
cd exercises/typescript && npm install && npm test   # Q2, Q10
```

| Exercise | Question | AI |
| --- | --- | --- |
| `python/journal_posting` | Q1 double-entry posting | Off |
| `python/bank_matching` | Q7 reconciliation proposals | Off for screens, on for onsite |
| `python/prepaid_amortization` | Q16 amortization schedule | On |
| `python/categorization_eval` | Q17 model evaluation | On |
| `typescript/trial_balance` | Q2 trial balance and P&L | Off |
| `typescript/period_close` | Q10 close state machine | Off |

## Depth

Every question carries three bars: **junior**, **senior**, **staff**. Ask the same stem for all candidates and climb the follow-ups until they stall. Don't hand juniors an easier domain — hand them the same ledger and stop earlier.
