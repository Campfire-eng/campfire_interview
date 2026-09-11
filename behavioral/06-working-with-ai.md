# Working with AI

This is not one of the five principles. It is a topic we cover in every behavioral loop
because it touches all of them. We build an AI product, we use AI tools every day, and the
job of a software engineer has changed because of them. We want to know how you use these
tools, how you judge what they produce, and what you think has changed and what has not.

## What we are listening for

- Real, current use. What tools they use, for what, and how that has changed in the last
  year.
- Judgment about output. They read what the tool produced, they know where it tends to be
  wrong, and they can describe a time they caught a mistake.
- Judgment about when not to use it. There are tasks where they choose to work without
  it, and they can say why.
- A clear view of what has changed in their job and what has not. Typing is faster.
  Deciding what to build, reviewing, and being responsible for the result are not.
- Responsibility for the result. If the tool wrote it and it was wrong, they treat that
  as their mistake.
- How they talk about it with teammates, including people who use these tools more or
  less than they do.

## Questions

### 1. Walk me through how you used AI tools on the last significant piece of work you shipped.

**Why we ask it.** We want a concrete, recent picture of how they actually work, not a
general view on AI.

**What a strong answer covers.** A specific task. Which parts they gave to the tool and
which they did themselves. How they checked the output. What the tool got wrong, and how
they noticed. Roughly how much time it saved, or did not.

**Follow-ups.** "What did the tool get wrong?" "How did you check it?" "What did you do
yourself, and why?" "What would this have looked like two years ago?"

**Weaker answers.** They describe the tool rather than the work. They cannot name anything
the tool got wrong. They do not use these tools and have not tried.

### 2. Tell me about a time an AI tool produced something that was wrong in a way that mattered. Did you catch it, and how?

**Why we ask it.** The main risk in using these tools is confident output that is wrong.
We want to see that they review carefully and know what kinds of errors to expect.

**What a strong answer covers.** A specific error with a real consequence, caught or not.
How it got past them, if it did. What they now check for that they did not before. If
they did not catch it, what happened next and how they handled it.

**Follow-ups.** "What kind of mistake was it?" "Why did it look right at first?" "What do
you check for now that you did not before?" "Who else reviewed it?"

**Weaker answers.** They have never seen the tool be wrong. They caught it, but cannot
say how. The mistake was shipped and the story treats the tool as responsible.

### 3. What parts of your job have changed because of AI tools, and what parts have not?

**Why we ask it.** We want to hear a considered view based on their own experience,
rather than a prediction.

**What a strong answer covers.** Specific changes: what they no longer do by hand, what
they do more of, how their day looks different. Specific things that have not changed:
deciding what to build, understanding the domain, reviewing, being responsible for the
result. An honest account of what they have lost, if anything, such as a skill they
practice less.

**Follow-ups.** "What do you spend more time on now?" "What do you spend less time on?"
"Is there a skill you are worse at than you were?" "What do you think will change next?"

**Weaker answers.** Everything has changed. Nothing has changed. The answer is about the
industry rather than about their own work.

### 4. Tell me about something you decided not to use AI for. Why?

**Why we ask it.** Knowing when not to use a tool is part of using it well. We want to
see the reasoning.

**What a strong answer covers.** A specific task and a specific reason: they needed to
understand it themselves, the cost of an error was too high, the tool was slower for
that task, or the output could not be checked. Whether the decision held up.

**Follow-ups.** "Would you make the same decision today?" "Was it slower?" "How did you
decide?"

**Weaker answers.** They use it for everything. They avoid it on principle and cannot
give a reason tied to the work.

### 5. How has AI changed how you review code, and how your code is reviewed?

**Why we ask it.** Review is where the quality of AI-produced code gets decided. We want
to see how they have adapted.

**What a strong answer covers.** Changes in what they look for, such as plausible code
that does not handle the actual case, tests that pass but do not test the right thing,
or code that duplicates something that already exists. How they tell a reviewer what was
generated and what was checked. How they handle a pull request that is larger than the
author has read.

**Follow-ups.** "Do you tell reviewers which parts were generated?" "Has review gotten
slower or faster?" "Tell me about a pull request you sent back because the author had
not read it."

**Weaker answers.** Review has not changed. They rely on the tool to review its own
output. They do not read generated code before sending it.

### 6. Tell me about a time AI tools let you do something you could not have done otherwise.

**Why we ask it.** These tools open up work that used to require a specialist. We want
to see them use that well and know its limits.

**What a strong answer covers.** A real example: a language they did not know, a domain
they were new to, a tool they had never used. How they made sure the result was right
without the expertise to judge it directly. Who they asked to check.

**Follow-ups.** "How did you know it was right?" "Who checked it?" "What did you learn
from it, and what did you not learn?"

**Weaker answers.** No example. The result was shipped without anyone who understood it
reviewing it. They describe it as learning the skill when they did not.

### 7. How do you handle differences on your team about how AI tools should be used?

**Why we ask it.** Teams disagree about this, and it can become a source of friction. We
want people who can work through it.

**What a strong answer covers.** A specific disagreement: someone using it too much,
someone refusing to use it, a junior engineer relying on it instead of learning. What
they said and did. Whether the team reached a shared standard, and what it was.

**Follow-ups.** "What was the other person's view?" "Did you agree on anything?" "How do
you help someone new learn the fundamentals when the tool will do it for them?"

**Weaker answers.** Everyone should use it the way they do. They avoided the conversation.
There is no example.
