# 8. ASC 606 schema and recognition schedule

| | |
| --- | --- |
| Track | Schema design + domain |
| Language | SQL, plus Python or TypeScript for schedule generation |
| Format | Design, optional code |
| AI | **Off** |
| Time | 50 min |

**The problem.** A SaaS customer signs an annual prepaid contract, upgrades mid-term, and
incurs usage overage. Design the tables and the job that recognizes revenue each period.

**Why we ask it.** Deferred revenue has to be a first-class balance. It should not be a
spreadsheet column that someone maintains by hand.

**What a strong answer covers.** Contract, invoice, a deferred revenue liability, and
monthly recognition journals. The main content is performance obligations (licence,
support, usage), standalone selling price allocation, modifications handled prospectively
or with catch-up (and asking us which one applies), a revenue waterfall, contract asset
versus contract liability, and every schedule line linked to a journal id. Further:
variable consideration and constraints, principal versus agent, multi-element arrangements
with credits, the difference between bookings, billings, cash, and revenue, deriving both
GAAP and non-GAAP ARR from the same facts, and what breaks when sales ops edits the
opportunity after invoices already exist.

**Follow-ups.** "They upgrade in month four and extend the term." "Usage is billed in
arrears." "Full refund in month seven."

**Common problems.** Recognizing cash as revenue. A `revenue_per_month` float on the
customer record. No performance obligations at all.

## Rubric

| Score | What it looks like |
| --- | --- |
| 1 | Cash is recognized as revenue when it arrives, or revenue lives as a revenue_per_month float on the customer record. There are no performance obligations. Deferred revenue is not a balance in the ledger. The design does not reach a coherent recognition job. |
| 2 | Contract, invoice, a deferred revenue liability, and monthly recognition journals are present. Performance obligations and standalone selling price allocation are missing or vague until asked. The upgrade, usage billed in arrears, and the refund are handled only once we raise them, and schedule lines are not tied to journal ids. |
| 3 | Performance obligations for licence, support, and usage are modeled with standalone selling price allocation. Modifications are handled prospectively or with catch-up, and the candidate asks which one applies. There is a revenue waterfall, contract asset is distinguished from contract liability, and every schedule line links to a journal id. The upgrade and extension, arrears billing, and month-seven refund are handled well. |
| 4 | Everything in 3, plus the candidate reaches the further material unprompted: variable consideration and constraints, principal versus agent, multi-element arrangements with credits, and the difference between bookings, billings, cash, and revenue. They can derive both GAAP and non-GAAP ARR from the same facts and explain what breaks when sales ops edits the opportunity after invoices already exist. Tradeoffs are stated. |
