# What the process looks like

Every stage stays in the same domain — books must balance, close must lock, AI output must
be reviewable. What changes from stage to stage is *how* we work together, not how hard
the accounting gets. There is no stage where we swap in an unrelated algorithm puzzle to
see if you are clever.

## Recruiter and hiring manager — 30 minutes

A conversation, not an evaluation of your ASC 606 knowledge. We want to hear whether
accounting genuinely interests you, whether you have empathy for controllers as users
(they are not consumers, and they are not developers), and how you feel about working in
person in San Francisco.

Bring questions. This is the stage where asking us what is actually hard about the product
is most useful to you.

## Technical screen — 60 minutes, one exercise, no AI

One hands-on exercise in a shared editor with the tests already in the repository. Which
one depends on the role:

| Role | Exercise |
| --- | --- |
| Backend / full-stack | Q1 journal posting (Python) or Q2 trial balance (TypeScript) |
| Product-leaning full-stack | Q10 period close (TypeScript) |
| Data / AI | Q7 bank matching (Python), run without AI at this stage |

You can read these exercises and their tests in [`exercises/`](exercises/) right now, and
you are welcome to attempt them beforehand — knowing the problem in advance does not spoil
anything, because we are going to talk through your reasoning either way.

What we pay attention to: the invariants you protect, what you name things, and what you
ask us before you start typing.

## Onsite — four sessions of 45–50 minutes

1. **Hands-on, AI allowed.** Q7 matching, Q17 model evaluation, Q16 amortization, or Q11
   flux. We are interested in how you verify that the books are right, not in whether the
   first draft compiled.
2. **Schema and backend, no AI.** Q3 GL schema, then either Q5 Stripe ingestion or Q8
   ASC 606.
3. **System design, no AI.** Q4 consolidation, Q9 multi-currency, or Q18 continuous close.
4. **Product or AI trust.** Q6 review queue, Q12 reconciliation workspace, Q13 Ember
   grounding, or Q19 model feedback loop.

For platform or security-leaning roles we swap in Q14 (permissions, segregation of duties,
approvals). When the role touches reporting or compliance we swap in Q20 (audit and
point-in-time reporting).

### Typical mixes by track

| Role | Sessions |
| --- | --- |
| Full-stack product | Q2 or Q10 hands-on, Q3 schema, Q6 review queue, Q12 recon workspace |
| Backend / platform | Q1 hands-on, Q3 schema, Q5 Stripe, Q14 permissions and approvals |
| Data engineering | Q7 hands-on, Q11 flux, Q15 duplicates, Q20 audit and point-in-time |
| AI engineering | Q17 hands-on eval, Q13 Ember grounding, Q19 feedback loop, plus Q1 without AI |

The AI engineering loop deliberately includes one ledger exercise run without AI. If you
are going to build autonomous accounting, you need to hold double-entry in your own head,
because you are the one reviewing what the model produced.

## Take-home — optional, 3–4 hours

Q7, Q11, Q16, or Q17. AI tools are explicitly allowed. We ask for a short write-up
covering the invariants you relied on, the failure modes you know about, and what you would
refuse to automate. Submissions with no tests and no mention of an audit trail are not
competitive, regardless of how the code looks.

## How we think about AI in the process

Some sessions are run without AI assistance and some allow it, and both are deliberate.

In the **AI-off** sessions we are checking that you own the domain model yourself. If a
model writes your posting logic, we learn nothing about whether *you* would have caught
the unbalanced journal.

In the **AI-on** sessions the tooling is genuinely allowed and we would rather see you use
it well than perform working without it. What we evaluate is your product sense, your
review quality, and whether you catch the accounting mistakes a model will happily ship —
plausible-looking code that quietly uses floats for money, or an evaluation that reports
one accuracy number.

Being fast with AI does not compensate for being loose with debits and credits. Working
carefully and protecting the ledger counts for a great deal, even if you cover less ground.
