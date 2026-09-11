# 12. Account reconciliation workspace

| | |
| --- | --- |
| Track | Product engineering |
| Language | TypeScript (API and UI contract) |
| Format | Design plus interface sketch |
| AI | **On** for the UI |
| Time | 45 min |

**The problem.** For GL cash versus bank, prepaid versus subledger, and accrued expenses:
a reconciliation has a GL balance, a supporting balance, reconciling items, and a
certification status. Design the API the Next.js app consumes.

**Why we ask it.** A reconciliation is a document with a tie-out and an approver. It is
more than a styled table.

**What a strong answer covers.** Fetching a reconciliation, listing items, certifying it.
Then: preparer and reviewer as two different people, balances frozen at
certification, reconciling item types (timing, error, unrecorded), attachments,
certification blocked when the variance exceeds policy, and the interaction with period
lock. Further out: continuous reconciliation versus a month-end packet, subledger identity
across systems, templates per account type, roll-forward schedules, auditor export, and
optimistic concurrency on certify.

**Follow-ups.** "The bank rec is two cents off." "The reviewer is also the preparer."

**Common problems.** Certifying without snapshotting the balance. Variance as a
free-text comment.
