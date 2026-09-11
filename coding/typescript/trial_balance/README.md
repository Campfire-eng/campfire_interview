# Trial balance and income statement

**Language:** TypeScript · **AI:** off · **Time:** ~45 minutes · **Starter:** `trial_balance.ts`

## Background

Every account in a chart of accounts has a **type**, and the type determines which
direction increases it:

| Type | Increased by | Normal balance |
| --- | --- | --- |
| `asset` | debit | debit |
| `expense` | debit | debit |
| `liability` | credit | credit |
| `equity` | credit | credit |
| `revenue` | credit | credit |

Two reports come out of the same posted lines:

- A **trial balance** is a point-in-time snapshot: for every account, the net of all lines
  posted with an effective date on or before a given date. Its defining property is that
  total debits equal total credits across the whole list. If they do not, something
  upstream is broken and every downstream report is in question.
- An **income statement** (P&L) is period activity, not a cumulative balance, and it
  covers revenue and expense accounts only. Assets, liabilities, and equity never appear
  on it.

The difference between "as of a date" and "between two dates" is the main point of the
exercise. They sound similar in English and produce very different numbers.

## Your task

Implement both exported functions in `trial_balance.ts`.

```ts
export function trialBalance(
  accounts: Account[],
  lines: JournalLine[],
  asOf: string,
): TrialBalanceRow[]

export function incomeStatement(
  accounts: Account[],
  lines: JournalLine[],
  periodStart: string,
  periodEnd: string,
): IncomeStatement
```

- `Account` is `{ id, name, type }` where type is one of the five above.
- `JournalLine` is `{ accountId, debitCents, creditCents, effectiveDate }`, with
  `effectiveDate` as a `YYYY-MM-DD` string. These sort and compare lexicographically, so
  you do not need a date library.
- `TrialBalanceRow` is `{ accountId, debitCents, creditCents }`.
- `IncomeStatement` is `{ revenueCents, expenseCents, netIncomeCents }`.

All amounts are integer cents.

### Rules the tests enforce

1. **`asOf` is inclusive and excludes everything after it.** With the fixture data, a
   trial balance as of `2026-03-31` nets `cash` to a 57,000 debit and `rev` to a 10,000
   credit. The `ar` account, which only has an April line, must be absent from the
   output entirely, not present with a zero balance.
2. **The trial balance balances.** Summing `debitCents` across all returned rows equals
   summing `creditCents`.
3. **The income statement is period activity.** For `2026-03-01` through `2026-03-31`:
   revenue 10,000, expense 3,000, net income 7,000. Both endpoints are inclusive. The
   January equity and cash lines do not appear, because those are balance sheet accounts,
   and neither does the April revenue, because it is outside the window.

Note that each account produces a single row. You choose which column its net lands in
based on the sign of the net. An account is not both a debit and a credit at once.

## Running the tests

```bash
cd coding/typescript
npm install
npx tsx --test trial_balance/trial_balance.test.ts
```

Or `npm test` to run this alongside the other TypeScript exercise.

## What we care about

The mapping from account type to normal balance should be explicit somewhere rather than
inferred from the sign of whatever happens to be in the data. We also notice whether you
ask which date field matters before you start. Real systems carry both an effective date
and a posted-at timestamp, and they answer different questions.

## Where the conversation usually goes

- Add gross margin, which means introducing a `cogs` subtype under expenses.
- Produce a December P&L when the books contain a January reversing accrual.
- Net income has to roll into equity. Where does that happen, and what does the balance
  sheet look like before it does?
- A controller clicks a revenue figure on the statement and wants the journals behind it.
- Why can you not compute the income statement by filtering the trial balance rows?

## Constraints

Integer cents only. Balance sheet accounts must never appear in the P&L. This exercise is
run without AI assistance. Language and standard library documentation is fine.
