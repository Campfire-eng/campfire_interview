import assert from "node:assert/strict";
import test from "node:test";
import { Books, CloseError } from "./period_close.ts";

test("accountant can post while open", () => {
  const books = new Books({ id: "2026-03", status: "open" });
  assert.deepEqual(books.postJournal("accountant"), { ok: true });
});

test("lock rejects posts", () => {
  const books = new Books({ id: "2026-03", status: "open" });
  books.beginClose("closer");
  books.lock("controller");
  assert.equal(books.getPeriod().status, "locked");
  assert.throws(() => books.postJournal("accountant"), CloseError);
});

test("accountant cannot post during closing; closer can", () => {
  const books = new Books({ id: "2026-03", status: "open" });
  books.beginClose("closer");
  assert.throws(() => books.postJournal("accountant"), CloseError);
  assert.deepEqual(books.postJournal("closer"), { ok: true });
});

test("reopen requires controller and a reason", () => {
  const books = new Books({ id: "2026-03", status: "open" });
  books.beginClose("controller");
  books.lock("controller");
  assert.throws(() => books.reopen("accountant", "oops"), CloseError);
  assert.throws(() => books.reopen("controller", "  "), CloseError);
  books.reopen("controller", "late AP invoice");
  assert.equal(books.getPeriod().status, "open");
  assert.deepEqual(books.postJournal("accountant"), { ok: true });
});
