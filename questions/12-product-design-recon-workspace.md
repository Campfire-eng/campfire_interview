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

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | The API is a styled table over rows. Certification does not snapshot the GL and supporting balances, so the certified numbers can drift after sign-off. Variance is a free-text comment rather than a computed figure. No notion of a preparer versus a reviewer. |
| 2 | Endpoints exist to fetch a reconciliation, list its items, and certify it. Variance is computed, but balances are not frozen at certification until asked. Preparer and reviewer roles, reconciling item types, and period lock only come up when prompted. |
| 3 | Fetch, list, and certify are designed with preparer and reviewer as two different people and balances frozen at certification. Reconciling items have types such as timing, error, and unrecorded, with attachments. Certification is blocked when the variance exceeds policy, and the interaction with period lock is handled. The two-cent and self-review follow-ups are answered cleanly. |
| 4 | Everything in 3, plus the further material without prompting: continuous reconciliation versus a month-end packet, subledger identity across systems, templates per account type, roll-forward schedules, auditor export, and optimistic concurrency on certify. Tradeoffs are stated. |
