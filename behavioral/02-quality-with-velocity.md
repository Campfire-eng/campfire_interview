# Quality with Velocity

> Deliver high-quality solutions swiftly to meet market demands.

## What we are listening for

There is a real tension in this principle. A ledger cannot be "mostly right" and a close
cannot be "roughly locked". At the same time, a startup that ships slowly falls behind.
We want engineers who know which corners can be cut and which cannot, and who can make
that call quickly and explain it to a teammate.

The specific things we listen for:

- A clear line between what must be correct on day one (money, permissions, the audit
  trail) and what can be rough at first (the UI, edge cases nobody has hit).
- Speed that comes from scoping and sequencing rather than from skipping tests.
- Willingness to ship something small and unpolished, and to say so in the pull request.
- Pushing back on a deadline when the thing being cut is one that cannot be cut.
- Cleaning up their own shortcuts, and being able to say which ones are still there.

We look out for two patterns: the engineer who is always fast and leaves work for others
to clean up, and the engineer who cannot ship without adding more than is needed.

## Questions

### 1. Tell me about a time you had to ship something faster than you were comfortable with. What did you cut, and what did you refuse to cut?

**Why we ask it.** This is the principle in one question. The answer tells us where they
draw the line and whether they draw it deliberately.

**What a strong answer covers.** A specific deadline with a real reason. They can name
what they dropped, such as scope, polish, or a nice-to-have, and what they protected:
correctness of the core path, tests on the invariants, a way to roll back. They told the
team what was being cut before it shipped. They can say which of the cuts they went back
and fixed.

**Follow-ups.** "Who decided what got cut?" "What broke?" "What is still cut today?"
"If the deadline had been a week later, what would you have done differently?"

**Weaker answers.** They cut tests. They cannot name what they protected. The shortcut
was not written down and someone else ran into it later. The deadline was self-imposed
and nothing much depended on it.

### 2. Describe a time you pushed back on a deadline. How did you make the case, and what happened?

**Why we ask it.** Velocity does not mean saying yes to everything. We want to see them
make the case for quality with evidence rather than with a general feeling of discomfort.

**What a strong answer covers.** They identified the specific thing that would go wrong if
it shipped on the date. Not "it will be rushed" but "the migration cannot be reversed and
we have not tested the reversal". They offered a smaller thing that could ship on time.
They accepted the outcome either way.

**Follow-ups.** "What exactly would have gone wrong?" "What did you offer instead?" "Were
you right?"

**Weaker answers.** The pushback was general. No alternative was offered. They describe
every deadline as unreasonable.

### 3. Tell me about a time you were reviewing a teammate's pull request and found something that would have caused a real problem. How did you handle it?

**Why we ask it.** Quality is a team property. Review is where it happens, and it is also
where working relationships can be strained. We want people who catch the problem and
keep the teammate's trust.

**What a strong answer covers.** They explained what would go wrong and how they knew,
in the review, in a tone the author could accept. They separated the blocking issue from
the style comments. If it was urgent they talked to the person instead of leaving a long
list of comments. They can describe how the author responded.

**Follow-ups.** "What did you write, roughly?" "Was there anything in the review you
decided not to say?" "How did the author take it?" "Did you check whether the same
problem existed elsewhere?"

**Weaker answers.** They approved it and fixed it later themselves. They blocked it on
style. The candidate focuses on having been right rather than on what the author learned.

### 4. Tell me about a time someone caught a significant problem in your code in review. What was it, and what did you do?

**Why we ask it.** This is the mirror of the previous question. We want to see how they
respond when a reviewer finds a problem in their work.

**What a strong answer covers.** A real catch with a real consequence avoided. They can
explain why they missed it. They thanked the reviewer and can name what they changed in
their own process, such as a test they now always write or a check they now always do.

**Follow-ups.** "Why did you miss it?" "Do you still miss that kind of thing?" "How did
you respond in the thread?"

**Weaker answers.** They cannot think of one. The catch was minor. They describe the
reviewer as difficult.

### 5. Tell me about a time you chose to slow down on something, and it turned out to be the right call, or the wrong one.

**Why we ask it.** Judgment shows most clearly when a choice costs something. We want to
know they can slow down on purpose, and whether they look back at that choice honestly
afterward.

**What a strong answer covers.** A specific reason to slow down, such as a migration on
money data, an integration with no sandbox, or a change to how permissions are checked.
What they did with the extra time. An honest account of whether it was worth it. A story
where it was not worth it is at least as useful as one where it was.

**Follow-ups.** "How did you explain the delay?" "What did you find in the extra time?"
"Looking back, how much of the extra time was necessary?"

**Weaker answers.** Every story is about being right to slow down. The slowdown was
perfectionism rather than risk. They cannot say what the delay cost.

### 6. How do you decide how much testing a change needs?

**Why we ask it.** The honest answer is "it depends", and we want to hear what it depends
on. This is the day-to-day form of the quality and velocity tradeoff.

**What a strong answer covers.** Different standards for different kinds of code, stated
clearly: anything touching money, permissions, or the audit trail gets tests on the
invariants before it merges; a UI tweak or an internal tool can go with less. An example
of each. An example of a change they undertested and regretted.

**Follow-ups.** "Give me an example of a change you shipped with no tests and were right
to." "Give me one where you were wrong." "How do you handle a teammate who tests less
than you think they should?"

**Weaker answers.** A single rule for everything. No example of undertesting. Testing
described as a gate imposed by others.
