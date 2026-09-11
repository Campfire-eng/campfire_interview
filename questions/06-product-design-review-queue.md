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

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | The review tool is a chat sidebar. There is no record of who accepted what. Auto-posting is on by default, or suggestions post without a human approving. Undo is a silent edit. |
| 2 | A suggestion list with accept, reject, edit, and paging is present, and who accepted what is recorded. Grouping, confidence with reasons, bulk accept, a keyboard flow, vendor history, and undo as reversal come up only when asked. Nothing is said about materiality or the model being wrong until prompted. |
| 3 | Similar transactions are grouped, confidence is shown with reasons, and bulk accept works under a threshold. The flow is keyboard-first with vendor history in context. Nothing auto-posts above policy and undo is a reversal rather than a silent edit. The $50 auto-approve, reviewer disagreement, and Miscellaneous drift follow-ups are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: materiality and risk cues such as new vendors, round-dollar amounts, period-end timing, and related parties, plus sampling of auto-approved items. The model that suggests is separated from the human who approves, and rejections feed learning without corrupting the chart of accounts. Empty, error, and partial-sync states are designed, and the candidate can say how the interface stays trustworthy when the model is wrong 8% of the time. |
