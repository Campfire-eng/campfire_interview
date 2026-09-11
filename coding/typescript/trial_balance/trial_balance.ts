export type AccountType = "asset" | "liability" | "equity" | "revenue" | "expense";

export type Account = {
  id: string;
  name: string;
  type: AccountType;
};

export type JournalLine = {
  accountId: string;
  debitCents: number;
  creditCents: number;
  effectiveDate: string; // YYYY-MM-DD
};

export type TrialBalanceRow = {
  accountId: string;
  debitCents: number;
  creditCents: number;
};

export type IncomeStatement = {
  revenueCents: number;
  expenseCents: number;
  netIncomeCents: number;
};

export function trialBalance(
  _accounts: Account[],
  _lines: JournalLine[],
  _asOf: string,
): TrialBalanceRow[] {
  throw new Error("not implemented");
}

export function incomeStatement(
  _accounts: Account[],
  _lines: JournalLine[],
  _periodStart: string,
  _periodEnd: string,
): IncomeStatement {
  throw new Error("not implemented");
}
