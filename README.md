# Campfire interview kit

This is everything we use to interview engineers at Campfire, published in full: the
questions, the process, the behavioral interview, and six exercises with runnable failing
tests. Nothing here is
withheld, and there is no hidden version.

We do that because our problems are not the kind you can spoil by reading about them in
advance. Campfire is an AI-native ERP — general ledger, multi-entity consolidation, bank
reconciliation, ASC 606 revenue recognition, period close, and Ember, the assistant that
answers questions about the books. The interesting parts are the invariants and the
judgment calls, and knowing what we are going to ask does not tell you what you would do
about a $2.50 bank fee that never made it into the general ledger.

We hire on **Python** and **TypeScript (Next.js / React)**. Every exercise is in one of
those. None of them are LeetCode.

## What's in here

| Path | What it is |
| --- | --- |
| [interview-kit.md](interview-kit.md) | All twenty questions: the problem, why we ask it, what a strong answer covers, and the follow-ups |
| [loop.md](loop.md) | The stages of the process and what happens in each one |
| [exercises/](exercises/) | Six starter folders with failing tests, each with its own detailed README |
| [behavioral/](behavioral/) | The behavioral interview: one file per core principle, with the questions we ask and what we listen for |

## Try the exercises

Every starter ships with failing tests, so the first thing you do is read the spec. Each
exercise folder has a README that explains the accounting background, the exact contract
you are implementing, what each test is checking, and where the conversation usually goes
afterwards.

```bash
# Python — Q1, Q7, Q16, Q17
pip install pytest
(cd exercises/python && pytest -q)

# TypeScript — Q2, Q10
(cd exercises/typescript && npm install && npm test)
```

| Exercise | Question | AI |
| --- | --- | --- |
| [`python/journal_posting`](exercises/python/journal_posting/) | Q1 — a journal that cannot unbalance the books | Off |
| [`python/bank_matching`](exercises/python/bank_matching/) | Q7 — reconciliation proposals | Off for the screen, on later |
| [`python/prepaid_amortization`](exercises/python/prepaid_amortization/) | Q16 — amortization schedule in whole cents | On |
| [`python/categorization_eval`](exercises/python/categorization_eval/) | Q17 — evaluating a GL-coding model | On |
| [`typescript/trial_balance`](exercises/typescript/trial_balance/) | Q2 — trial balance and P&L | Off |
| [`typescript/period_close`](exercises/typescript/period_close/) | Q10 — close as a state machine | Off |

You are welcome to work through these before an interview. If you do, come ready to talk
about the decisions you made rather than to re-type the solution.

## What we cover

System design, schema design, product engineering, backend engineering, data engineering,
and AI engineering — plus the controls work an ERP forces on you: permissions, segregation
of duties, and auditability.

## AI in the interview

Some sessions are run **without AI** and some **with it**, and both are on purpose. The
AI-off sessions exist so we can see that you personally hold the domain model — that you
know why a journal must balance and what a locked period protects. The AI-on sessions are
genuinely AI-on: use the tools, and expect us to review the output together, because
catching the accounting bug a model confidently shipped is the actual job.

[loop.md](loop.md) says which sessions are which.

## Do you need to know accounting?

No. Most people we hire did not, and several of these questions explain the concept in the
prompt. What we need is that you treat the domain as real. A ledger has invariants that
software cannot negotiate with, and "close enough" arithmetic ends up in someone's audit
file. If that sounds interesting rather than tedious, you will enjoy these problems.
