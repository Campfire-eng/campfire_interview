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
| [questions/](questions/) | All twenty questions, one file each: the problem, why we ask it, what a strong answer covers, and the follow-ups |
| [loop.md](loop.md) | The stages of the process and what happens in each one |
| [coding/](coding/) | Six starter folders with failing tests, each with its own detailed README |
| [system-design/](system-design/) | Five system design challenges, each with a prompt, background, follow-ups, and a rubric |
| [behavioral/](behavioral/) | The behavioral interview: one file per core principle, with the questions we ask and what we listen for |

## The questions

| # | Type | Question |
| --- | --- | --- |
| 1 | coding | [Post a journal that cannot unbalance the books](questions/01-coding-journal-posting.md) |
| 2 | coding | [Trial balance and a P&L from the same lines](questions/02-coding-trial-balance.md) |
| 3 | schema | [Schema for a real general ledger](questions/03-schema-gl-schema.md) |
| 4 | system-design | [Multi-entity consolidation without the spreadsheet](questions/04-system-design-consolidation.md) |
| 5 | system-design | [Stripe: from webhook to native connector](questions/05-system-design-stripe-connector.md) |
| 6 | product-design | [AI categorization review queue](questions/06-product-design-review-queue.md) |
| 7 | coding | [Score bank transactions against GL candidates](questions/07-coding-bank-matching.md) |
| 8 | schema | [ASC 606 schema and recognition schedule](questions/08-schema-asc-606.md) |
| 9 | system-design | [Multi-currency: functional versus reporting](questions/09-system-design-multi-currency.md) |
| 10 | coding | [Period close as a state machine](questions/10-coding-period-close.md) |
| 11 | coding | [Flux analysis pipeline](questions/11-coding-flux-pipeline.md) |
| 12 | product-design | [Account reconciliation workspace](questions/12-product-design-recon-workspace.md) |
| 13 | ai-design | [Ember: answers that can go in the audit file](questions/13-ai-design-ember-grounding.md) |
| 14 | system-design | [Permissions, segregation of duties, and approval workflows](questions/14-system-design-permissions-and-approvals.md) |
| 15 | coding | [Duplicate detection across integrations](questions/15-coding-duplicate-detection.md) |
| 16 | coding | [Prepaid amortization engine](questions/16-coding-prepaid-amortization.md) |
| 17 | coding | [Evaluate the categorization model like an accountant](questions/17-coding-model-evaluation.md) |
| 18 | system-design | [Continuous close and autonomous reconciliation](questions/18-system-design-continuous-close.md) |
| 19 | ai-design | [The feedback loop that trains the accounting model](questions/19-ai-design-model-feedback-loop.md) |
| 20 | system-design | [Point-in-time reports, audit log, and who changed the books](questions/20-system-design-point-in-time-and-audit.md) |

The [questions index](questions/README.md) has the tags, how a session runs, and a
coverage map showing which tracks each question serves.

## Try the exercises

Every starter comes with failing tests, so the first step is to read the spec. Each
exercise folder has a README that explains the accounting background, the contract you
are implementing, what each test checks, and what we usually talk about afterwards.

```bash
# Python: four exercises
pip install pytest
(cd coding/python && pytest -q)

# TypeScript: two exercises
(cd coding/typescript && npm install && npm test)
```

Each exercise is the starter for one question in the [question catalog](questions/).
The catalog has twenty questions, numbered 1 to 20, and six of them have starters.

| Exercise | Topic | Catalog question | AI |
| --- | --- | --- | --- |
| [`python/journal_posting`](coding/python/journal_posting/) | A journal that cannot unbalance the books | 1 | Off |
| [`python/bank_matching`](coding/python/bank_matching/) | Reconciliation proposals | 7 | Off for the screen, on later |
| [`python/prepaid_amortization`](coding/python/prepaid_amortization/) | Amortization schedule in whole cents | 16 | On |
| [`python/categorization_eval`](coding/python/categorization_eval/) | Evaluating a GL-coding model | 17 | On |
| [`typescript/trial_balance`](coding/typescript/trial_balance/) | Trial balance and P&L | 2 | Off |
| [`typescript/period_close`](coding/typescript/period_close/) | Close as a state machine | 10 | Off |

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
