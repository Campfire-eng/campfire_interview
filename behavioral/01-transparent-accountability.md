# Transparent Accountability

> Maintain openness in our operations and take responsibility for our actions and
> decisions.

## What we are listening for

We build software that other people rely on to be correct. If problems are hidden in how
we work, they end up hidden in the product too. So we want people who share
bad news early, in writing, with the people it affects, and who describe their own
mistakes in the first person without being asked.

The specific things we listen for:

- Saying "I" when describing what went wrong and "we" when describing what went right,
  rather than the other way around.
- Telling people a deadline will slip before it slips.
- Writing things down where others can see them: decisions, status, incidents, tradeoffs.
- Owning the outcome of a decision even when the decision was reasonable at the time.
- Being open about what they do not know in front of people who are more senior.

We also notice the opposite pattern: stories where the candidate was right, the problem
was someone else, and the resolution was that the other person came around.

## Questions

### 1. Tell me about a bug you shipped that affected real users. Walk me through what happened from the moment you found out.

**Why we ask it.** Most engineers have shipped a bug that reached users. What we want to
hear is the sequence: how they found out, who they told, how quickly, what they told the
affected users, and what they changed.

**What a strong answer covers.** They found out, they told the team and the affected
customers before being asked, they said what they knew and what they did not, they fixed
it, and they wrote up how it got through. They can describe the writeup. They can say
which part was their own error in plain terms.

**Follow-ups.** "Who told the customer, and what did they say?" "What did the postmortem
say was the cause, and do you agree with it?" "What would you do differently, and have you
done that differently since?"

**Weaker answers.** The bug was found by someone else and the candidate's role starts at
the fix. The cause is described as a process or a tool with no person involved. The
customer communication is skipped or handed to "the account team" with no detail.

### 2. Tell me about a time you had to tell someone senior to you that a plan or deadline was not going to work.

**Why we ask it.** In many organizations, deadlines slip without anyone saying so ahead
of time. We need people who say it out loud, early, and with a proposal.

**What a strong answer covers.** They raised it as soon as they believed it, not when it
became obvious to everyone. They came with evidence and a concrete alternative, such as
cutting scope, moving the date, or adding someone. They can describe how the conversation
went, including the pushback.

**Follow-ups.** "How far in advance did you raise it?" "What was their first reaction?"
"Was there a point where you considered not saying anything?" "Did the alternative you
proposed happen?"

**Weaker answers.** They raised it the day before. They raised it as a complaint with no
proposal. They made it work through extra hours and describe that as the win.

### 3. Describe a decision you made that turned out to be wrong. How did you find out, and what did you do about it?

**Why we ask it.** We want to see the difference between a bad decision and a bad
outcome, and whether they take responsibility for the outcome either way.

**What a strong answer covers.** A real decision with a real cost. They can say what they
knew at the time and what they should have found out. They told the people affected,
reversed or mitigated it, and can describe what changed in how they decide now. They do
not overclaim. A reasonable call that went badly is described as exactly that.

**Follow-ups.** "Who was affected and how did they hear about it?" "Was it a bad decision
or a bad outcome?" "What did you do the next time you had a similar call?"

**Weaker answers.** The wrong decision turns out to have been right in hindsight. The
candidate cannot name one. The cost fell entirely on someone else and the candidate
describes it from a distance.

### 4. Tell me about a time you disagreed with a decision, it went ahead anyway, and you had to carry it out.

**Why we ask it.** Accountability includes owning decisions you argued against. We want
to see whether they can carry something out well after losing the argument, and how they
talked about it afterward.

**What a strong answer covers.** They made their case clearly and in the right forum. Once
it was decided, they stopped reopening the question and did the work well. If it turned
out badly, they did not say "I told you so" to the team. If it turned out well, they can
say so.

**Follow-ups.** "How did you make the case?" "What did you say to your team about the
decision after it was made?" "Did it turn out the way you expected?"

**Weaker answers.** They did it slowly or badly to make a point. They complained to peers
rather than to the decision-maker. They cannot describe the other side's reasoning
fairly.

### 5. Tell me about a time you found out something was wrong that nobody else had noticed yet. What did you do?

**Why we ask it.** Small problems matter in our product. We need people who will mention
a problem even when it is awkward to bring up.

**What a strong answer covers.** They checked enough to be sure it was real, then raised
it quickly with the right people, in a form others could verify. They did not hold it
back because it was awkward, because it was someone else's area, or because it would
create work.

**Follow-ups.** "How sure were you before you raised it?" "Whose area was it?" "What
happened to the person whose code or process it was?"

**Weaker answers.** The problem was fixed without telling anyone. It was raised in a way
that blamed someone in public. It was not mentioned until a full fix was ready.

### 6. How do you keep the people who depend on your work informed about where it stands?

**Why we ask it.** This is the everyday form of transparency. Most people answer with
"standup" and "Slack". We want to hear what they do when the news is not good.

**What a strong answer covers.** Written status that someone could read without asking
them. Clear flags when confidence drops. Telling the people who depend on them about a
risk before it becomes a delay. A specific example of a status update that was hard to
write.

**Follow-ups.** "Tell me about the last status update you sent that you did not want to
send." "How does someone on another team find out what you are working on without asking
you?"

**Weaker answers.** Status is only shared when someone asks. Updates are all green until
they are red. The candidate describes a process rather than a habit.
