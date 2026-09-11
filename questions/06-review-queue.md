# 6. AI categorization review queue

| | |
| --- | --- |
| Track | Product engineering + AI |
| Language | TypeScript / React |
| Format | Product design, optional component sketch |
| AI | **On** for the UI sketch |
| Time | 45 min |

**The problem.** The model proposes account, vendor, department, and class for roughly
100k bank lines a month. Controllers need to review about twice as fast without missing
material errors. Design the review experience and the data the UI needs behind it.

**Why we ask it.** Human-in-the-loop design for a system of record is the core product bet.
It is also a hard interface problem.

**What a strong answer covers.** A suggestion list with accept, reject, edit, and paging is
the starting point. What makes it good: grouping similar transactions, confidence shown
with reasons, bulk accept under a threshold, a keyboard-first flow, vendor history in
context, nothing auto-posting above policy, and undo implemented as a reversal rather than
a silent edit. The strongest versions bring in materiality and risk cues (new vendor,
round-dollar amounts, period-end timing, related parties), sampling of auto-approved
items, separation between the model that suggests and the human who approves, learning
from rejections without corrupting the chart of accounts, empty and error and partial-sync
states, and how the interface stays trustworthy when the model is wrong 8% of the time.

**Follow-ups.** "Auto-approve anything under $50." "Two reviewers disagree." "The model
starts coding everything to Miscellaneous."

**Common problems.** A chat sidebar as the review tool. No record of who accepted
what. Auto-posting on by default.
