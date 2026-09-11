# The question catalog

These are the twenty problems we draw from. You will see four or five of them, not all
twenty. We publish the whole set on purpose. None of the questions has a trick, and none
of them rewards having seen the question before. We would rather you spend your
preparation time reading about the domain than guessing what we might ask.

Everything here is in the same domain: an AI-native ERP with a general ledger,
multi-entity consolidation, bank reconciliation, ASC 606 revenue recognition, period
close, and Ember, the assistant that answers questions about the books. The languages are
Python and TypeScript / Next.js / React, because that is what we build in.

You do not need to be an accountant. Several of these questions explain the accounting
concept in the prompt itself, and in the live sessions we are glad to explain more. What
we look for is whether you take the domain seriously.

## How a session runs

We read the problem together, then you drive. Ask us questions. What we ask for is
usually underspecified in the same way a real ticket is, and noticing that is part of the
work. Think out loud. If you go down a path and change your mind, say so. Seeing you
correct course tells us more than a clean first draft.

The follow-ups listed under each question are the directions the conversation tends to
go. They are not a checklist you need to finish. Running out of time on them is normal.

## Tags

| Tag | Meaning |
| --- | --- |
| AI-off | No generative AI, no Copilot, no autocomplete that writes logic. Language and library documentation is fine. |
| AI-on | LLM and Copilot allowed. You own the output — expect to review it with us line by line. |
| Pair | Shared editor, 45–50 minutes. |
| Design | Whiteboard or shared doc, 45–50 minutes. |
| Take-home | 3–4 hours, with written invariants required. |

**On the AI-off sessions.** These sessions are not a statement that we dislike AI tooling.
We build an AI product and we use these tools daily. They exist because we need to see
that you understand the domain yourself. That is the judgment you will use when you
review what a model wrote.

## The questions

One file per question. Each has the problem, why we ask it, what a strong answer covers,
the follow-ups, common problems, and a rubric. Starter paths are relative to the
repository root.

## How the rubric works

Every question ends with a rubric that scores the answer from 1 to 4 and describes what
an answer at each level looks like for that question.

| Score | Meaning |
| --- | --- |
| 1 | Breaks a core invariant of the question or does not reach a coherent answer. |
| 2 | Basic and mostly correct. Covers the first points of a strong answer, with gaps that are filled only when we ask. |
| 3 | Solid. Covers the main points on its own and handles the follow-ups well. |
| 4 | Everything in 3, plus the deeper material reached without prompting, with tradeoffs stated. |

Interviewers record the score and the specific evidence for it. A 3 is a good result. A 4
is uncommon in 45 minutes and is not required for a hire. A 1 on a question run without AI
is the result we weigh most, because it usually means the candidate does not hold the
domain model the question tests.

| # | Type | Question |
| --- | --- | --- |
| 1 | coding | [Post a journal that cannot unbalance the books](01-coding-journal-posting.md) |
| 2 | coding | [Trial balance and a P&L from the same lines](02-coding-trial-balance.md) |
| 3 | schema | [Schema for a real general ledger](03-schema-gl-schema.md) |
| 4 | system-design | [Multi-entity consolidation without the spreadsheet](04-system-design-consolidation.md) |
| 5 | system-design | [Stripe: from webhook to native connector](05-system-design-stripe-connector.md) |
| 6 | product-design | [AI categorization review queue](06-product-design-review-queue.md) |
| 7 | coding | [Score bank transactions against GL candidates](07-coding-bank-matching.md) |
| 8 | schema | [ASC 606 schema and recognition schedule](08-schema-asc-606.md) |
| 9 | system-design | [Multi-currency: functional versus reporting](09-system-design-multi-currency.md) |
| 10 | coding | [Period close as a state machine](10-coding-period-close.md) |
| 11 | coding | [Flux analysis pipeline](11-coding-flux-pipeline.md) |
| 12 | product-design | [Account reconciliation workspace](12-product-design-recon-workspace.md) |
| 13 | ai-design | [Ember: answers that can go in the audit file](13-ai-design-ember-grounding.md) |
| 14 | system-design | [Permissions, segregation of duties, and approval workflows](14-system-design-permissions-and-approvals.md) |
| 15 | coding | [Duplicate detection across integrations](15-coding-duplicate-detection.md) |
| 16 | coding | [Prepaid amortization engine](16-coding-prepaid-amortization.md) |
| 17 | coding | [Evaluate the categorization model like an accountant](17-coding-model-evaluation.md) |
| 18 | system-design | [Continuous close and autonomous reconciliation](18-system-design-continuous-close.md) |
| 19 | ai-design | [The feedback loop that trains the accounting model](19-ai-design-model-feedback-loop.md) |
| 20 | system-design | [Point-in-time reports, audit log, and who changed the books](20-system-design-point-in-time-and-audit.md) |

## Coverage map

| # | Question | System | Schema | Product | Backend | Data | AI eng | AI policy | Hands-on | Lang |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| 1 | Journal posting | | | | x | | | Off | code | Py |
| 2 | Trial balance / P&L | | | x | x | | | Off | code | TS |
| 3 | GL schema | | x | | | | | Off | | SQL |
| 4 | Consolidation | x | | | | | | Off | | — |
| 5 | Stripe webhooks → connector | x | | x | x | | | Off | sketch | Py + TS |
| 6 | Review queue | | | x | | | x | On | sketch | TS |
| 7 | Bank matching | | | | x | x | | On/Off | code | Py |
| 8 | ASC 606 | | x | | x | | | Off | optional | both |
| 9 | Multi-currency | x | | | | | | Off | | — |
| 10 | Period close | | | x | x | | | Off | code | TS |
| 11 | Flux pipeline | | | | | x | | On | code | Py |
| 12 | Recon workspace | | | x | x | | | On | | TS |
| 13 | Ember grounding | x | | | | | x | Mixed | | Py |
| 14 | Permissions, SoD, approvals | | x | x | x | | | Off | optional | TS/SQL |
| 15 | Duplicate detection | | | | x | x | x | On | code | Py |
| 16 | Prepaid amortization | | | | x | | | On | code | Py |
| 17 | Model evaluation | | | | | x | x | On | code | Py |
| 18 | Continuous close | x | | | | | x | Off | | — |
| 19 | Model feedback loop | x | | | | x | x | On | sketch | Py |
| 20 | Audit and point-in-time | | x | | | x | | Off | | Py + SQL |

**Questions with starter code and failing tests:** 1, 2, 7, 10, 16, 17. These are the ones
you can work through in this repository before you talk to us.

**Run without AI:** 1, 2, 3, 4, 5, 8, 9, 10, 14, 18, 20. Every loop includes at least two.

**AI engineering track:** 6, 13, 17, 19, with 15 and 18 close by.
