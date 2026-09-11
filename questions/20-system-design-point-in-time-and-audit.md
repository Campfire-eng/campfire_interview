# 20. Point-in-time reports, audit log, and who changed the books

| | |
| --- | --- |
| Track | Data engineering, platform, compliance |
| Language | Python and SQL |
| Format | Design |
| AI | **Off** |
| Time | 45 min |

**The problem.** Auditors want the P&L as it existed on February 14, when the board pack
went out, versus as it exists now after late adjustments. They also want every AI
suggestion, every accept and reject, and every period lock.

**Why we ask it.** This question is about bi-temporality and evidence. An ERP needs full
history, at a level that an analytics dashboard does not.

**What a strong answer covers.** Timestamps and an activity log. Then: posted journals
immutable; report runs stored with their parameters and their results; as-of queries that
distinguish `effective_date` from `posted_at`; late postings distinguished from
restatement. Further: valid time versus transaction time; snapshotting versus replaying
from an event log, with the cost trade made explicit; retention; tamper evidence; deleting
a user who approved a reconciliation without destroying the evidence; and every AI answer
citing a report run id rather than a live query.

**Follow-ups.** "They restated Q1 in July." "Delete the user who approved this
reconciliation."

**Common problems.** Mutating journal lines and relying on `updated_at`. No stored
report definition. Treating git history as an audit log.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Journal lines are mutated in place and history relies on updated_at. There is no stored report definition, so the February 14 P&L cannot be reproduced. Git history or a generic activity log is offered as the audit log. The design does not reach as-of queries. |
| 2 | Timestamps and an activity log capture who changed what. Posted journals may still be editable, and report runs are not stored with their parameters and results until asked. As-of queries do not distinguish effective_date from posted_at, and late postings are not separated from restatement without prompting. |
| 3 | Posted journals are immutable. Report runs are stored with their parameters and their results. As-of queries distinguish effective_date from posted_at, and late postings are distinguished from restatement. The follow-ups on the Q1 restatement in July and deleting an approving user are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: valid time versus transaction time, and snapshotting versus replaying from an event log with the cost trade made explicit. Retention, tamper evidence, and deleting a user without destroying the evidence of what they approved are covered. Every AI answer cites a report run id rather than a live query. Tradeoffs are stated. |
