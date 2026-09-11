import assert from "node:assert/strict";
import test from "node:test";
import { incomeStatement, trialBalance, type Account, type JournalLine } from "./trial_balance.ts";

const accounts: Account[] = [
  { id: "cash", name: "Cash", type: "asset" },
  { id: "ar", name: "AR", type: "asset" },
  { id: "rev", name: "Revenue", type: "revenue" },
  { id: "rent", name: "Rent", type: "expense" },
  { id: "eq", name: "Common stock", type: "equity" },
];

const lines: JournalLine[] = [
  { accountId: "cash", debitCents: 50_000, creditCents: 0, effectiveDate: "2026-01-01" },
  { accountId: "eq", debitCents: 0, creditCents: 50_000, effectiveDate: "2026-01-01" },
  { accountId: "cash", debitCents: 10_000, creditCents: 0, effectiveDate: "2026-03-05" },
  { accountId: "rev", debitCents: 0, creditCents: 10_000, effectiveDate: "2026-03-05" },
  { accountId: "rent", debitCents: 3_000, creditCents: 0, effectiveDate: "2026-03-31" },
  { accountId: "cash", debitCents: 0, creditCents: 3_000, effectiveDate: "2026-03-31" },
  { accountId: "ar", debitCents: 4_000, creditCents: 0, effectiveDate: "2026-04-02" },
  { accountId: "rev", debitCents: 0, creditCents: 4_000, effectiveDate: "2026-04-02" },
];

test("trial balance as of March 31 ignores April", () => {
  const rows = trialBalance(accounts, lines, "2026-03-31");
  const byId = Object.fromEntries(rows.map((r) => [r.accountId, r]));
  assert.equal(byId.cash.debitCents - byId.cash.creditCents, 57_000);
  assert.equal(byId.rev.creditCents - byId.rev.debitCents, 10_000);
  assert.equal(byId.ar, undefined);
  const debit = rows.reduce((s, r) => s + r.debitCents, 0);
  const credit = rows.reduce((s, r) => s + r.creditCents, 0);
  assert.equal(debit, credit);
});

test("March income statement", () => {
  const pl = incomeStatement(accounts, lines, "2026-03-01", "2026-03-31");
  assert.equal(pl.revenueCents, 10_000);
  assert.equal(pl.expenseCents, 3_000);
  assert.equal(pl.netIncomeCents, 7_000);
});
