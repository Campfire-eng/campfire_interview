# System design

The onsite includes one 45-minute system design session. We pick one of the five
challenges in this folder based on the role. Each challenge file has the prompt we give
you, some background on the accounting involved, what we ask you to produce, the
follow-ups we tend to ask, and a rubric that says what good and weak answers look like.

| Challenge | File | Usually for |
| --- | --- | --- |
| Multi-entity consolidation | [01-consolidation.md](01-consolidation.md) | Backend, platform |
| Multi-currency ledger | [02-multi-currency.md](02-multi-currency.md) | Backend, platform |
| Continuous reconciliation pipeline | [03-continuous-reconciliation.md](03-continuous-reconciliation.md) | AI engineering, data |
| Point-in-time reporting and audit log | [04-point-in-time-and-audit.md](04-point-in-time-and-audit.md) | Data, platform, compliance |
| Period close across many entities | [05-period-close-orchestration.md](05-period-close-orchestration.md) | Full-stack product, backend |

## How the session runs

You get the prompt, a whiteboard or shared document, and 45 minutes. No AI tools. We
spend the first few minutes on questions. The prompt is underspecified on purpose, and we
want to see what you ask before you start drawing.

Then you drive. We expect to see, in roughly this order:

1. The requirements you are designing for, including the ones you decided to leave out.
2. The data model. What is stored, what is immutable, and what can change.
3. The main flow. How data gets in, how it is processed, and how it gets out.
4. The controls. Who can do what, what the system refuses to do, and what is recorded.
5. Failure cases. What happens when something arrives twice, arrives late, or is wrong.
6. Scale, if there is time. Where the load is and what you would do about it.

We ask follow-ups throughout. Some add a requirement. Some describe something going wrong.
We are interested in how the design absorbs the change, and in whether you can say what
would have to change.

You do not need to know accounting in advance. Each challenge explains the concepts it
uses, and we will explain more in the session. What we need is that you take the
constraints seriously once they are explained.

## Rubric

Every challenge is scored on the same six areas. The challenge files give specific
examples for each. This table gives the general shape.

| Area | Strong | Adequate | Weak |
| --- | --- | --- | --- |
| Requirements | Asks clarifying questions, states assumptions, names what is out of scope, and identifies the constraint that matters most. | Asks some questions and states some assumptions. | Starts drawing immediately. Designs for requirements the prompt did not give. |
| Data model | Separates immutable financial records from mutable reference data. Every amount has a currency and a precision. Every record can be traced to its source. | The main entities are present and correctly related. Some ambiguity about what can change. | Amounts as floats. Records edited in place. No way to trace a figure back to where it came from. |
| Correctness | Names the invariants the system must hold and shows where each one is enforced. | Names the invariants but enforcement is vague or lives in the client. | Does not name invariants. Correctness is assumed. |
| Controls and audit | Every change has an actor, a time, and a reason. Automated actions are recorded with what produced them. Some actions require a human. | An audit log exists. Its contents and coverage are not specified. | No audit trail, or one that can be edited. Automation with no human step and no record. |
| Failure handling | Duplicate, late, out-of-order, and incorrect inputs are handled explicitly. Corrections are additive, not destructive. Replay is possible. | Some failure cases are handled. Others are noticed when we ask. | Happy path only. Corrections by deleting or overwriting. |
| Communication | Clear diagrams, clear names, and a running account of tradeoffs. Changes the design when a follow-up warrants it and says what changed. | Understandable with some prompting. | Hard to follow. Defends the first design against every follow-up. |

We do not expect a strong result in all six areas in 45 minutes. A strong session usually
has strong results in three or four, adequate in the rest, and no weak ones in data model
or correctness. Weak results in those two areas are the ones we take most seriously,
because they are the hardest to fix later.

## What we are not looking for

We are not looking for a specific architecture. Several very different designs can be
strong answers to each of these challenges. We are also not looking for you to cover
everything in the rubric. We would rather see a smaller design that is correct and
well-reasoned than a larger one with gaps in the fundamentals.
