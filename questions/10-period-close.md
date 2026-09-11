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
