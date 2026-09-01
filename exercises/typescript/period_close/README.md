# Period close state machine

**Language:** TypeScript · **AI:** off · **Time:** ~45 minutes · **Starter:** `period_close.ts`

## Background

At the end of an accounting period the books get **closed**: activity stops, the numbers
are finalized, and the period's reports become something the company will stand behind
externally. Closing is not a single moment. It runs through states:

- **`open`** — normal operation. Anyone with posting rights books entries.
- **`closing`** — the soft close. The team is tying out reconciliations and booking
  accruals, and ordinary day-to-day posting has to stop or the numbers keep moving
  underneath them. Only people doing close work may post.
- **`locked`** — the hard close. Nothing posts at all. This is the state auditors rely on.

Occasionally a period must be **reopened** — a late vendor invoice genuinely belongs in
the month that just closed. That is allowed, but it is a controlled act: it takes
authority and it takes a stated reason, because someone will eventually ask why the March
numbers changed after March was closed.

This is a control system. Every rule below is a control, and controls that live only in
the UI are not controls.

## Your task

Implement the four methods on the `Books` class in `period_close.ts`. Throw `CloseError`
for anything you reject.

```ts
beginClose(actor: Role): void
lock(actor: Role): void
reopen(actor: Role, reason: string): void
postJournal(actor: Role): { ok: true }
```

`Role` is `"accountant" | "closer" | "controller"`. `PeriodStatus` is
`"open" | "closing" | "locked"`. `getPeriod()` already returns a copy of the current
period and is implemented for you.

### Rules the tests enforce

| Status | Who may post |
| --- | --- |
| `open` | accountant, closer, controller |
| `closing` | closer (and controller); **not** accountant |
| `locked` | nobody |

1. **Posting while open succeeds** for an accountant, returning `{ ok: true }`.
2. **Locking blocks posting.** After `beginClose` then `lock`, `getPeriod().status` is
   `"locked"` and `postJournal("accountant")` throws `CloseError`.
3. **During `closing`, an accountant is refused and a closer succeeds.**
4. **Reopen requires a controller and a real reason.** `reopen("accountant", "oops")`
   throws on authority. `reopen("controller", "  ")` throws on the reason — whitespace is
   not a reason. `reopen("controller", "late AP invoice")` succeeds, returns the period to
   `open`, and an accountant can post again.

Decide deliberately what `beginClose` and `lock` require, and whether the transitions can
be skipped. The tests always call `beginClose` before `lock`; whether you permit locking
a period that was never in `closing` is your call to make and defend.

## Running the tests

```bash
cd exercises/typescript
npm install
npx tsx --test period_close/period_close.test.ts
```

Or `npm test` to run this alongside the other TypeScript exercise.

## What we care about

The valid transitions and the role checks should be legible — someone reading this file
should be able to reconstruct the policy without executing it. Failures should say what
was refused and why, since these errors end up in front of a controller. Think about what
the class would need to record, not just enforce: a reopen with a reason that nobody
stores has not really been controlled.

## Where the conversation usually goes

- Two accountants post at the exact instant the lock lands. What guarantees the lock wins?
- A late AP invoice belongs in a month that is already locked. Reopen, or book an
  adjusting entry in the current period?
- Different subsidiaries close on different days. Is status per entity, per book, or both?
- An automated process wants to post accruals during `closing`. Under what policy, and how
  do you know later that it was the automation?
- What is the difference between a soft close and a hard lock in terms of what it protects?

## Constraints

Do not implement close by deleting and rebuilding the period's entries. Enforcement
belongs in this layer, not in a form that disables a button. This exercise is run without
AI assistance.
