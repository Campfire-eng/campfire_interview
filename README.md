# Campfire interview kit

This repository has the material we use to interview engineers at Campfire: the
questions, how the process works, the behavioral interview, and six coding exercises with
tests. Our interviewers use the same material.

We publish it because reading the questions ahead of time does not give you the answers.
Campfire is an AI-native ERP. It covers the general ledger, multi-entity consolidation,
bank reconciliation, ASC 606 revenue recognition, period close, and Ember, the assistant
that answers questions about the books. The questions are about judgment. Knowing the
question in advance still leaves you to work through it.

We hire for Python and TypeScript (Next.js / React). Every exercise uses one of those. The
exercises are based on real problems from our product.

## What's in here

| Path | What it is |
| --- | --- |
| [interview-kit.md](interview-kit.md) | All twenty questions: the problem, why we ask it, what a strong answer covers, and the follow-ups |
| [loop.md](loop.md) | The stages of the process and what happens in each one |
| [exercises/](exercises/) | Six starter folders with failing tests, each with its own detailed README |
| [behavioral/](behavioral/) | The behavioral interview: one file per core principle, with the questions we ask and what we listen for |

## Try the exercises

Every starter comes with failing tests, so the first step is to read the spec. Each
exercise folder has a README that explains the accounting background, the contract you
are implementing, what each test checks, and what we usually talk about afterwards.

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

You are welcome to work through these before an interview. If you do, be ready to talk
about the decisions you made. That is more useful to us than seeing the solution typed
out again.

## What we cover

System design, schema design, product engineering, backend engineering, data engineering,
and AI engineering. We also cover the controls work that comes with an ERP: permissions,
segregation of duties, and auditability.

## AI in the interview

Some sessions are run without AI and some with it. Both are on purpose. The AI-off
sessions let us see that you understand the domain yourself. In the AI-on sessions you
should use the tools. We will review the output together, because reviewing what a model
produces is a large part of the job.

[loop.md](loop.md) says which sessions are which.

## Do you need to know accounting?

No. Most people we hire did not, and several of these questions explain the concept in the
prompt. What we need is that you take the domain seriously. If that sounds interesting to
you, you will probably enjoy these problems.
