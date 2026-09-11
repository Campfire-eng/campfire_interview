# 3. Schema for a real general ledger

| | |
| --- | --- |
| Track | Schema design |
| Language | SQL (types can be discussed in either language) |
| Format | Design |
| AI | **Off** |
| Time | 45 min |

**The problem.** Design tables for chart of accounts, journals, journal lines, accounting
periods, and entities (subsidiaries). The customer has 40 entities, roughly 2M lines a
year, and auditors who will ask who changed what and when.

**Why we ask it.** A ledger is a set of append-only financial facts next to mutable
dimensions. The schema either respects that split or works against it for a long time.

**What a strong answer covers.** `accounts`, `journals`, and `journal_lines` with real
foreign keys; debit and credit columns, or a signed amount with a check constraint you can
explain; period on the journal. Then: `entity_id` on every fact, period status
(`open / soft-close / locked`), a unique idempotency key, `effective_date` versus
`created_at`, postable versus header accounts, and audit columns. The deeper version gets
into partitioning and indexing by entity and period, immutability via reversal journals,
monotonic sequence numbers for audit, chart of accounts versioning, dimensions
(department, class, location) as a posting-dimension table instead of 40 nullable columns,
and supporting multiple books (GAAP versus tax) without cloning the schema.

**Follow-ups.** "We need departments and classes." "We acquired a company mid-year with a
different chart of accounts." "Reopen January after it was locked."

**Common problems.** A mutable `amount` on lines. No period concept at all. Account
names as free text on lines. Choosing a document store because the ledger "is just
events."

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Lines carry a mutable amount with no way to tell what changed. There is no period concept, or account names are free text on lines. The design reaches for a document store because the ledger is just events, and cannot answer who changed what and when. |
| 2 | accounts, journals, and journal_lines exist with real foreign keys, and either debit and credit columns or a signed amount with a check constraint the candidate can explain. Period is on the journal. entity_id on facts, period status, an idempotency key, effective_date versus created_at, header accounts, and audit columns are missing until asked. |
| 3 | entity_id is on every fact, periods have open, soft-close, and locked states, and there is a unique idempotency key. effective_date and created_at are separate, header accounts cannot be posted to, and audit columns are present. The departments and classes, mid-year acquisition, and reopen January follow-ups are handled well. |
| 4 | Everything in 3, plus the deeper material unprompted: partitioning and indexing by entity and period at 2M lines a year, immutability through reversal journals, and monotonic sequence numbers for audit. Dimensions live in a posting-dimension table rather than nullable columns, the chart of accounts is versioned, and multiple books fit without cloning the schema. Tradeoffs are stated. |
