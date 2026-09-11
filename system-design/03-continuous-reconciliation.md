# Continuous reconciliation pipeline

| | |
| --- | --- |
| Time | 45 min |
| Format | Whiteboard or shared document |
| AI | Off |
| Usually for | AI engineering, data engineering |

## The prompt

Today the finance team reconciles bank accounts once a month. They export bank
transactions, match them against the ledger by hand, and post entries for anything the
ledger is missing, such as bank fees and interest. The team has three people and
thousands of transactions a month across 40 bank accounts, two card programs, and
Stripe.

Design a pipeline that ingests bank, card, and Stripe activity as it happens, proposes
matches and entries, lets the team review and post them, and keeps a record that would
satisfy an auditor. A model produces the proposals. The finance team stays in control.

## Background

- **Reconciliation** means confirming that the ledger's record of a bank account agrees
  with the bank's record. Every bank transaction should correspond to a ledger entry, and
  differences have to be explained.
- **Matching** pairs a bank transaction with a ledger entry. Amounts may differ by fees.
  One payment may cover several invoices. Dates differ because of settlement delays.
- **Proposed entries** are entries the system suggests for bank activity the ledger does
  not have, such as fees, interest, or a payment that was never recorded.
- **Posting** makes an entry part of the books. Once posted, an entry is not edited. It is
  reversed by another entry if it was wrong.
- **Periods** are locked after close. Nothing posts into a locked period.

The point of the design is that the system can propose a great deal and post very
little on its own. What it does automatically has to be visible, reversible, and
explainable.

## What we ask you to produce

- The flow from an event at the bank or Stripe to a posted entry and a reconciled item.
- The states an item can be in, and who or what moves it between states.
- What the model produces, what it is allowed to do on its own, and what it is not.
- How the review queue is ordered and what a reviewer sees.
- What is recorded for each automated action, and how a day of events could be replayed.

## Follow-ups

- "The customer redesigned their chart of accounts and the model's proposals got worse
  overnight. How do you find out, and what happens?"
- "Unmatched items are ten days old and the period closes in two days."
- "Stripe sends the same payout event twice, a day apart."
- "An auditor asks why a specific bank fee was posted to a specific account with no human
  involved."

## Rubric

| Area | Strong | Weak |
| --- | --- | --- |
| Requirements | Asks what the team is willing to let the system post without review, and what they are not. Asks about volume, latency, and what the auditor needs. Decides early that proposals and posted entries are different things. | Designs a fully automatic system. Does not ask what should require a human. |
| Data model | Proposals are a separate record from posted entries, with a state, a source event, the model version and inputs that produced them, and who or what acted on them. Bank events are stored as received, with an idempotency key. Match records link bank items to ledger entries and can be many-to-many. | Proposals are written straight into the ledger. Bank events are transformed on the way in and the original is lost. Matching is one-to-one only. |
| Correctness | Names the invariants: every posted entry balances, nothing posts into a locked period, a bank item is matched at most once, and the same source event never posts twice. Shows where each is enforced. | Automated posting bypasses period checks. Duplicate events post twice. Matched items can be matched again. |
| Controls and audit | Every automated action records the reason, the model and policy version, the confidence, and a way to reverse it. Thresholds are per account and per type. There is a way to turn automation off for an account or entirely. Certification of a reconciliation records what was automated. | No record of why an action was taken. A single global threshold. No way to stop automation without a deploy. |
| Failure handling | Duplicate and out-of-order events are handled by design. A model quality drop is detected by monitoring acceptance rates and unmatched aging, not by a customer complaint. Replay from stored events is possible and idempotent. Backpressure is considered. | Happy path only. Model quality is assumed. Replay would double-post. |
| Communication | Draws the states and transitions clearly. Separates what the model does from what the system enforces. Can answer the auditor follow-up with a specific record. | Mixes model behavior with system behavior. Cannot say what record would answer the auditor. |
