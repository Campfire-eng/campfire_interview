# 10. Period close as a state machine

| | |
| --- | --- |
| Track | Backend + product engineering |
| Language | TypeScript |
| Format | Pair |
| AI | **Off** |
| Time | 45 min |
| Starter | `coding/typescript/period_close` |

**The problem.** Implement period statuses `open → closing → locked`, plus a `reopen` that
requires a reason and an actor. Posting fails while locked. During `closing`, only a
closer role may post accruals.

**Why we ask it.** Close is a control system. It is more than a boolean flag on a row.

**What a strong answer covers.** A status enum with guards on posting, then role checks, a
persisted reopen audit record, no skipping `closing`, checklist preconditions such as
completed reconciliations, and correct behavior when a post races the lock. The fuller
discussion covers soft close versus hard lock, adjusting entries as an alternative to
reopening, entity-level versus book-level status, the close calendar, and what automation
is allowed to post during close, under which policy, and stamped with which run id.

**Follow-ups.** "Two accountants post at the exact lock instant." "A late AP invoice
belongs in a locked month."

**Common problems.** Deleting and rebuilding the month. Enforcing the lock only in
the UI.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | The lock is enforced only in the UI, or the month is closed by deleting and rebuilding it. Status is a boolean rather than a state machine, so closing can be skipped and reopen leaves no record. Posting can succeed while the period is locked. |
| 2 | A status enum exists and posting is guarded against locked periods. Role checks during closing and the reopen audit record are thin or missing until asked. No thought given to skipping closing, checklist preconditions, or a post racing the lock until we raise them. |
| 3 | The status enum, posting guards, role checks, and a persisted reopen record with reason and actor all work, and closing cannot be skipped. Checklist preconditions such as completed reconciliations are enforced. The candidate gives correct behavior when two accountants post at the lock instant and handles the late AP invoice well when asked. |
| 4 | Everything in 3, plus the candidate reaches the fuller discussion unprompted: soft close versus hard lock, adjusting entries as an alternative to reopening, entity-level versus book-level status, and the close calendar. They can say what automation is allowed to post during close, under which policy, and stamped with which run id. Tradeoffs are stated and code is clean and tested. |
