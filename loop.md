# What the process looks like

Every stage stays in the same domain — books must balance, close must lock, AI output must
be reviewable. What changes from stage to stage is *how* we work together, not how hard
the accounting gets. There is no stage where we swap in an unrelated algorithm puzzle to
see if you are clever.

The whole loop, in order:

| Stage | Length | Format |
| --- | --- | --- |
| Recruiter screen | 30 min | Conversation |
| Hiring manager screen | 30 min | Conversation, with some technical and behavioral questions |
| Virtual technical screen | 45 min | Code review and bug fixing in a shared editor |
| Onsite: system design | 45 min | Whiteboard or shared doc |
| Onsite: programming exercise 1 | 45 min | Shared editor, AI off |
| Onsite: programming exercise 2 | 45 min | Shared editor, AI on |
| Onsite: behavioral | 30 min | Conversation |

## Recruiter screen — 30 minutes

A conversation about the role, the team, compensation, and logistics, including how you
feel about working in person in San Francisco. We will also want a sense of why accounting
software interests you. This is not an evaluation of your ASC 606 knowledge.

Bring questions. This is the stage where asking us what is actually hard about the product
is most useful to you.

## Hiring manager screen — 30 minutes

Three things packed into half an hour, so expect us to move quickly:

1. **Pitch.** We tell you what Campfire is building and why we think an AI-native ERP is
   the right bet. Push back on it.
2. **Technical.** A few questions about work you have actually done — a system you own,
   a bug you chased, a decision you would make differently now. We may pull one thread
   into the domain: what would you want a ledger to refuse to do?
3. **Behavioral.** How you have handled disagreement, ambiguity, and being wrong. We want
   empathy for controllers as users — they are not consumers, and they are not developers.
   The questions come from [`behavioral/`](behavioral/), usually the Customer-Centric
   Innovation and Growth Mindset files.

## Virtual technical screen — 45 minutes, code review and bug fixing, no AI

We give you a working-looking piece of code from the same domain as the exercises in
[`exercises/`](exercises/) — journal posting, trial balance, period close — and it has
bugs in it. Some are obvious, some are the kind that only show up as an unbalanced trial
balance three months later. You review it the way you would review a teammate's pull
request: read it, tell us what is wrong and why it matters, and fix what you can in the
time available.

The invariants the bugs violate are the ones the exercise READMEs spell out, so reading
those beforehand is genuinely useful preparation. Knowing the problem in advance does not
spoil anything, because we are going to talk through your reasoning either way.

What we pay attention to: whether you find the bugs that corrupt the books before the ones
that merely look untidy, how you explain a defect to someone who did not write the code,
and what you check before you call a fix done.

## Onsite — four sessions

### System design — 45 minutes, no AI

One of Q4 consolidation, Q9 multi-currency, or Q18 continuous close. For platform or
security-leaning roles we swap in Q14 (permissions, segregation of duties, approvals).
When the role touches reporting or compliance we swap in Q20 (audit and point-in-time
reporting). Product-leaning roles may get Q6 review queue or Q12 reconciliation workspace
instead.

We care about the invariants you name before you draw boxes, and what you refuse to
let the system do.

### Programming exercise 1 — 45 minutes, no AI

One hands-on exercise with the tests already in the repository:

| Role | Exercise |
| --- | --- |
| Backend / full-stack | Q1 journal posting (Python) or Q2 trial balance (TypeScript) |
| Product-leaning full-stack | Q10 period close (TypeScript) |
| Data / AI | Q1 journal posting (Python) |

You can read these exercises and their tests in [`exercises/`](exercises/) right now, and
you are welcome to attempt them beforehand. If you do, come ready to talk about the
decisions you made rather than to re-type the solution.

### Programming exercise 2 — 45 minutes, AI allowed

Q7 bank matching, Q16 prepaid amortization, Q17 model evaluation, or Q11 flux. Use the
tools. We are interested in how you verify that the books are right, not in whether the
first draft compiled, and we will review the model's output together.

### Behavioral — 30 minutes

A conversation with someone you would work alongside, drawn from the questions in
[`behavioral/`](behavioral/). There is one file per core principle, and this session
usually goes deep on two or three of them — most often Transparent Accountability and
Collaborative Excellence, since by now we have seen you code and want to know what you
are like to ship with. Concrete stories beat principles: a time you shipped something
that was wrong and what you did next, a time you disagreed with a decision and how it
resolved, a time you had to learn a domain from zero.

### Typical mixes by track

| Role | Design | Exercise 1 (no AI) | Exercise 2 (AI on) |
| --- | --- | --- | --- |
| Full-stack product | Q6 review queue or Q12 recon workspace | Q2 or Q10 | Q7 or Q16 |
| Backend / platform | Q4 consolidation or Q14 permissions | Q1 | Q7 or Q16 |
| Data engineering | Q20 audit and point-in-time | Q1 | Q7 or Q11 |
| AI engineering | Q13 Ember grounding or Q19 feedback loop | Q1 | Q17 |

Every track includes at least one ledger exercise run without AI. If you are going to
build autonomous accounting, you need to hold double-entry in your own head, because you
are the one reviewing what the model produced.

## How we think about AI in the process

The technical screen, the system design session, and the first programming exercise are
run without AI. The second programming exercise allows it. Both are deliberate.

In the **AI-off** sessions we are checking that you own the domain model yourself. If a
model writes your posting logic, we learn nothing about whether *you* would have caught
the unbalanced journal.

In the **AI-on** session the tooling is genuinely allowed and we would rather see you use
it well than perform working without it. What we evaluate is your product sense, your
review quality, and whether you catch the accounting mistakes a model will happily ship —
plausible-looking code that quietly uses floats for money, or an evaluation that reports
one accuracy number.

Being fast with AI does not compensate for being loose with debits and credits. Working
carefully and protecting the ledger counts for a great deal, even if you cover less ground.
