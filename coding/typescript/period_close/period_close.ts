export type PeriodStatus = "open" | "closing" | "locked";

export type Role = "accountant" | "closer" | "controller";

export type Period = {
  id: string;
  status: PeriodStatus;
};

export class CloseError extends Error {}

export class Books {
  constructor(private period: Period) {}

  getPeriod(): Period {
    return { ...this.period };
  }

  beginClose(actor: Role): void {
    throw new Error("not implemented");
  }

  lock(actor: Role): void {
    throw new Error("not implemented");
  }

  reopen(actor: Role, reason: string): void {
    throw new Error("not implemented");
  }

  postJournal(actor: Role): { ok: true } {
    throw new Error("not implemented");
  }
}
