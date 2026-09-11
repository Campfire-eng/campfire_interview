# Multi-currency ledger

| | |
| --- | --- |
| Time | 45 min |
| Format | Whiteboard or shared document |
| AI | Off |
| Usually for | Backend, platform |

## The prompt

A company operates in Germany and keeps its books in EUR. Its parent reports in USD.
Vendors bill it in GBP, customers pay through Stripe, which settles in USD, and it holds
bank accounts in EUR, USD, and GBP. Exchange rates come from a daily feed.

Design how the ledger stores amounts, how rates are managed, how gains and losses from
currency movements are recorded, and how statements are produced in both EUR and USD.

## Background

A few concepts the design needs:

- **Functional currency** is the currency an entity keeps its books in. Here it is EUR.
  Every entry is recorded in EUR, even if the transaction happened in another currency.
- **Transaction currency** is the currency the transaction actually happened in. A GBP
  invoice is recorded in EUR at the rate on the invoice date, and the original GBP amount
  is kept too.
- **Realized gain or loss** happens when a foreign-currency item is settled at a different
  rate than it was recorded at. If a GBP invoice was recorded at one rate and paid at
  another, the difference is a gain or loss.
- **Unrealized gain or loss** happens at period end. Open foreign-currency balances, such
  as unpaid invoices and foreign bank accounts, are revalued at the period-end rate, and
  the difference is recorded. This is reversed or adjusted when the item is settled.
- **Reporting currency** is what the parent wants to see. Translating EUR statements into
  USD uses different rates for different kinds of accounts, and the resulting difference
  goes to a specific equity account.

## What we ask you to produce

- How an amount is stored on a journal line.
- The rate table: what it is keyed by, where rates come from, and how corrections work.
- The flow for a GBP vendor invoice from receipt through payment, including the realized
  gain or loss.
- Period-end revaluation: what is revalued, what is not, and what entries are produced.
- How a USD income statement is produced from EUR books.

## Follow-ups

- "March is closed. On April 2 the rate feed restates the March 31 rate."
- "The company holds cash in a currency that is not its functional currency. What happens
  at period end?"
- "A customer pays a EUR invoice in USD through Stripe, and Stripe takes a fee in USD."
- "Show me the entries that explain why the USD balance sheet moved this month when
  nothing was posted in EUR."

## Rubric

| Area | Strong | Weak |
| --- | --- | --- |
| Requirements | Asks which currency is functional and which is reporting. Asks where rates come from and how often. Asks whether the customer needs to explain FX movements to an auditor. | Treats currency as a display concern. Does not distinguish functional from reporting currency. |
| Data model | Each line stores the transaction currency and amount, the functional currency amount, and a reference to the rate used. Rates are keyed by currency pair, date, and source, and are never overwritten. Precision is per currency. | A single amount column in one currency. Rates stored as a single current value. Amounts as floats. |
| Correctness | Names the invariants: every journal balances in the functional currency, foreign amounts are never summed across currencies, revaluation only applies to monetary items, and every rate used is identifiable. Distinguishes realized from unrealized correctly. | Revalues everything, including equity and fixed assets. Sums amounts across currencies. Cannot say which rate a figure used. |
| Controls and audit | Rates for closed periods are frozen. A rate correction after close creates a new rate version and any effect is posted in the open period. Every FX entry cites the rate identifiers it used. | Rate corrections change historical figures. FX entries have no reference to a rate. |
| Failure handling | Handles a missing rate for a date explicitly, such as by refusing to post or by flagging. Handles a restated rate without touching closed periods. Handles settlement in a third currency. | Falls back to the latest rate silently. Reposts closed periods when a rate changes. |
| Communication | Walks through one transaction end to end with numbers. Shows the entries at each step. Explains why the USD balance sheet can move without EUR postings. | Stays abstract. Cannot produce the entries for the invoice example. |
