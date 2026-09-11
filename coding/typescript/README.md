# TypeScript exercises

Two self-contained exercises. Each folder has a starter module, a test file that acts as
the specification, and a README that explains the accounting problem and the contract you
are implementing.

| Folder | Exercise | AI |
| --- | --- | --- |
| [`trial_balance/`](trial_balance/) | Trial balance as of a date, plus a period income statement | Off |
| [`period_close/`](period_close/) | Period close as a state machine with roles | Off |

## Setup

Node 18 or newer. Tests run on the built-in `node:test` runner through `tsx`, so there is
no Jest or Vitest configuration to learn.

```bash
cd coding/typescript
npm install
```

## Running

```bash
npm test                                            # both exercises
npx tsx --test trial_balance/trial_balance.test.ts  # one exercise
```

Both suites start red, throwing `not implemented`. That is intentional. The failing test
tells you what the function is supposed to do.

## Before you start

Read the exercise README first, then the test file, then the starter module. Money is
integer cents in both exercises. Dates are `YYYY-MM-DD` strings that compare correctly
with `<` and `>`, so no date library is needed. If something in the spec is unclear, ask.
Deciding what to clarify is part of the exercise.
