# Period close across many entities

| | |
| --- | --- |
| Time | 45 min |
| Format | Whiteboard or shared document |
| AI | Off |
| Usually for | Full-stack product, backend |

## The prompt

A customer has 40 entities. Each entity closes its books monthly. A close involves a
checklist of tasks: reconciliations, accruals, depreciation, intercompany confirmation,
and review. Some tasks depend on others. Some depend on tasks in other entities. The
group close depends on every entity being closed. Right now the process is tracked in a
spreadsheet, people post entries into periods that were supposed to be closed, and the
group controller finds out about problems by asking.

Design the system that runs the close: the period states, the checklist and its
dependencies, the locking rules, and the view the group controller uses to see where
things stand.

## Background

- A **period** is a month, quarter, or year for one entity. It moves through states. A
  typical set is open, closing, soft-closed, and locked. In a soft-closed period only
  certain people can post. In a locked period nobody can.
- A **close checklist** is the list of tasks that have to be done before a period can be
  locked. Each task has an owner, a status, and evidence, such as a reconciliation
  certificate or a posted entry.
- **Dependencies** run between tasks. Depreciation runs before the fixed asset
  reconciliation. Intercompany confirmation needs both entities to have posted their side.
- **Reopening** a locked period happens, and has to be controlled. It requires a reason
  and an approver, and everything that depended on the period being locked has to be
  considered again.

## What we ask you to produce

- The period state model and the rules for each transition, including who can trigger it.
- The checklist model: tasks, owners, dependencies within and across entities, and
  evidence.
- How posting is controlled by period state, and where that check lives.
- What happens when a locked period is reopened.
- The group controller's view: what it shows and how it stays current.

## Follow-ups

- "Entity 12 locked January. Entity 30 then finds an intercompany entry with entity 12
  that was never posted."
- "The depreciation run failed halfway through for six entities."
- "Two people try to lock the same period at the same time."
- "An auditor asks who reopened November, why, and what was posted before it was locked
  again."

## Rubric

| Area | Strong | Weak |
| --- | --- | --- |
| Requirements | Asks what soft-close means for this customer and who can post during it. Asks how cross-entity dependencies are handled today. Asks whether tasks are entity-specific or shared templates. | Designs a task list with no notion of period state. Does not ask about reopening. |
| Data model | Periods are per entity with an explicit state and a transition history. Tasks reference a period, an owner, dependencies, and evidence. Dependencies can cross entities. Checklist templates are separate from checklist instances. | Period state is a boolean. Tasks are free-form. No history of state changes. Dependencies exist only in the UI. |
| Correctness | Names the invariants: nothing posts into a locked period, a period cannot lock with incomplete required tasks, and the group cannot close with an open entity. The posting check is enforced in the ledger, not in the client. State transitions are atomic. | Locking is a flag the UI checks. Posting into a locked period is possible through another path. Concurrent locks both succeed. |
| Controls and audit | Every transition records actor, time, and reason. Reopening requires a reason and an approver and is visible in the audit trail. Postings during soft close are restricted by role and recorded. | Anyone can reopen. Reopening leaves no trace. Soft close is unenforced. |
| Failure handling | A failed automated task, such as depreciation, is idempotent and can be re-run for the affected entities without double-posting. Reopening re-evaluates dependent tasks and the group close. Concurrent transitions are serialized. | Re-running a failed task double-posts. Reopening does not affect anything downstream. Concurrency is not considered. |
| Communication | Draws the state machine and the dependency graph clearly. Explains where the posting check lives and why. Adjusts the design for the intercompany follow-up and says what changes. | State machine is unclear. Cannot say where posting is blocked. Cross-entity follow-up has no answer. |
