# Point-in-time reporting and audit log

| | |
| --- | --- |
| Time | 45 min |
| Format | Whiteboard or shared document |
| AI | Off |
| Usually for | Data engineering, platform, compliance |

## The prompt

On February 14 the finance team sent the January income statement to the board. In March,
they posted late adjustments to January. The auditors now want two things: the January
income statement exactly as the board saw it on February 14, and the January income
statement as it stands today, with an explanation of every difference. They also want a
complete record of every change to the books, every period lock and unlock, and every
suggestion the AI assistant made along with whether it was accepted.

Design the storage and query model that supports this.

## Background

Two different times matter for every financial record:

- **Effective date** is when the transaction belongs, in accounting terms. A late
  adjustment posted in March can have an effective date in January.
- **Posted time** is when the record was actually written to the books.

A report "as of February 14" means: include every record whose effective date is in
January and whose posted time is on or before February 14. A report "as of today" includes
records posted since. The difference between the two is the late adjustments.

Posted entries are immutable. A wrong entry is corrected by posting a reversing entry and
a new one, not by editing. This is what makes as-of reporting possible.

An **audit log** records who did what and when. For an ERP it has to cover more than data
changes: period locks, permission changes, report generation, and automated actions.

## What we ask you to produce

- How journal entries are stored so that both times are queryable.
- How a report run is stored so it can be reproduced exactly.
- The query for "January as of February 14" and for "January as of now".
- What the audit log contains, what writes to it, and how it is protected.
- How AI suggestions and their outcomes are recorded.

## Follow-ups

- "They restated all of Q1 in July. How is that different from a late adjustment?"
- "Delete the user who approved this reconciliation. Privacy law requires it."
- "The AI assistant answered a question about January revenue last week. What did it see,
  and can you prove it?"
- "The audit log is now larger than the ledger. What do you do?"

## Rubric

| Area | Strong | Weak |
| --- | --- | --- |
| Requirements | Asks whether reports need to be reproducible exactly or approximately. Asks what the auditor needs to see about AI involvement. Asks about retention and about who can read the audit log. | Treats it as adding a timestamp column. Does not ask what the auditor actually needs. |
| Data model | Journal entries carry both effective date and posted time. Entries are immutable. Report runs are stored with their parameters, the as-of time, and either the result or enough to regenerate it exactly. The audit log is append-only and separate from the data it describes. | Entries have an updated-at column and are edited in place. Reports are computed live with nothing stored. The audit log is a table anyone with write access can modify. |
| Correctness | Names the invariants: posted entries never change, an as-of query at the same time always returns the same result, and every audit event has an actor and a time. Distinguishes a late adjustment from a restatement. | As-of results can change when new data arrives. Restatement handled by editing old entries. |
| Controls and audit | The audit log covers data changes, period locks and unlocks, permission changes, report runs, and AI suggestions with their outcome. It is tamper-evident. Actors are recorded by stable identifier so a deleted user's actions remain attributable. AI answers cite a stored report run rather than a live query. | The audit log only covers data changes. Deleting a user deletes their history. AI answers cannot be reproduced. |
| Failure handling | Handles the deleted-user case without destroying evidence. Handles audit log growth with a stated retention and archival approach. Considers snapshot versus replay from an event log and states the tradeoff. | Deleting a user cascades. No plan for growth. Snapshots and event logs conflated. |
| Communication | Writes out the as-of query. Explains the difference between the two report views with a concrete example. Clear about what is stored versus computed. | Cannot produce the query. Vague about what a stored report run contains. |
