# What the process looks like

Every stage uses the same domain. What changes from stage to stage is how we work
together, not the difficulty of the domain. None of the stages use an unrelated algorithm
puzzle.

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
feel about working in person in San Francisco. We also want to hear why accounting
software interests you. This is not a test of your ASC 606 knowledge.

Bring questions. This is a good stage to ask us what is hard about the product.

## Hiring manager screen — 30 minutes

Three things in half an hour, so we move quickly:

1. **Pitch.** We tell you what Campfire is building and why we think an AI-native ERP is
   the right bet. You are welcome to push back.
2. **Technical.** A few questions about work you have done: a system you own, a bug you
   tracked down, a decision you would make differently now. We may take one of these into
   the domain, for example what you would want the system to refuse to do.
3. **Behavioral.** How you have handled disagreement, ambiguity, and being wrong. We want
   to see empathy for our users, who are accounting professionals rather than consumers
   or developers. The questions come from [`behavioral/`](behavioral/), usually the
   Customer-Centric Innovation and Growth Mindset files.

## Virtual technical screen — 45 minutes, code review and bug fixing, no AI

We give you a piece of code from the same domain as the exercises in
[`coding/`](coding/), such as journal posting, trial balance, or period close. It
looks like it works, but it has bugs in it. Some are easy to see. Others only show up
later. You review it the way you would review a
teammate's pull request: read it, tell us what is wrong and why it matters, and fix what
you can in the time available.

The bugs break the invariants that the exercise READMEs describe, so reading those
beforehand is useful preparation. Knowing the problem in advance does not spoil anything,
because we talk through your reasoning in the session.

We pay attention to whether you find the bugs that produce wrong results before the ones
that are only cosmetic, how you explain a defect to someone who did not write the code, and
what you check before you call a fix done.

## Onsite — four sessions

### System design — 45 minutes, no AI

The five challenges we choose from are in [`system-design/`](system-design/), each with
the prompt, the follow-ups, and the rubric we score against. Which one you get depends on
the role. Backend and platform roles usually get consolidation or multi-currency. AI and
data roles usually get the continuous reconciliation pipeline or point-in-time reporting.
Full-stack product roles usually get period close across many entities. For platform or
security-leaning roles we sometimes use the permissions and approvals question (number
14 in the [question catalog](interview-kit.md)) instead, and product-leaning roles may get
the review queue (6) or reconciliation workspace (12) question.

We care about the invariants you name before you draw boxes, and about what you decide
the system should not allow.

### Programming exercise 1 — 45 minutes, no AI

One hands-on exercise with the tests already in the repository:

| Role | Exercise |
| --- | --- |
| Backend / full-stack | Journal posting (Python) or trial balance (TypeScript) |
| Product-leaning full-stack | Period close (TypeScript) |
| Data / AI | Journal posting (Python) |

You can read these exercises and their tests in [`coding/`](coding/) now, and you
are welcome to try them beforehand. If you do, be ready to talk about the decisions you
made. That is more useful to us than seeing the solution typed out again.

### Programming exercise 2 — 45 minutes, AI allowed

Bank matching, prepaid amortization, or model evaluation, all in Python. Use the tools. We are interested in how you check that the output is correct, not in whether the
first draft compiled. We will review the model's output together.

### Behavioral — 30 minutes

A conversation with someone you would work with, based on the questions in
[`behavioral/`](behavioral/). There is one file per core principle. This session usually
goes deep on two or three of them, most often Transparent Accountability and
Collaborative Excellence, because by now we have seen you code and want to know what you
are like to work with. Specific stories are more useful than general principles: a time
you shipped something that was wrong and what you did next, a time you disagreed with a
decision and how it was resolved, a time you had to learn a new domain from scratch.

### Typical mixes by track

| Role | Design | Exercise 1 (no AI) | Exercise 2 (AI on) |
| --- | --- | --- | --- |
| Full-stack product | Period close across many entities | Trial balance or period close | Bank matching or prepaid amortization |
| Backend / platform | Consolidation or multi-currency | Journal posting | Bank matching or prepaid amortization |
| Data engineering | Point-in-time reporting and audit log | Journal posting | Bank matching |
| AI engineering | Continuous reconciliation pipeline | Journal posting | Model evaluation |

Every track includes at least one exercise run without AI, so we can see how you work
without the tools.

## How we think about AI in the process

The technical screen, the system design session, and the first programming exercise are
run without AI. The second programming exercise allows it. Both are on purpose.

In the AI-off sessions we are checking that you understand the domain yourself. If a
model writes the code, we cannot tell whether you would have noticed the mistakes in it.

In the AI-on session the tools are allowed, and we want to see you use them well rather
than avoid them. We look at your product sense, your review quality, and whether you
catch the mistakes a model can produce.

Speed with AI tools is useful, but it does not make up for incorrect results. We would
rather see careful, correct work, even if it covers less ground.
