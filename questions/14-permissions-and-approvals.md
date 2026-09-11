# 14. Permissions, segregation of duties, and approval workflows

| | |
| --- | --- |
| Track | Platform, schema, security |
| Language | Verbal plus SQL or TypeScript types |
| Format | Design, optional state-machine code |
| AI | **Off** |
| Time | 50 min |

**The problem.** The product advertises granular permissions in the low thousands, plus
approval workflows. A user may post journals under $10k but not lock periods, and may see
the P&L but not payroll accounts. Manual journals, vendor bills, and high-value AI
suggestions all require approval. Design authorization and the approval workflow together.

**Why we ask it.** Authorization has to work at data grain. Workflow is part of the ledger
lifecycle, not something added afterwards.

**What a strong answer covers.** Roles mapped to permissions and checked on routes, with a
submit-approve-post flow. Then: resource, action, and condition (amount, account range,
entity); deny by default; every grant audited; assistant tools re-checking authorization
instead of trusting the chat session; multi-step approvals with thresholds, delegation,
reject-with-reason, an immutable snapshot of what the approver saw, and no
self-approval. Going deeper: segregation-of-duties conflicts across prepare, approve, and
lock; keeping thousands of flags maintainable through groups and implied permissions with
fixture-based tests; per-entity roles for the same user; break-glass access; policy stored
as versioned data; evidence export for auditors; and AI-drafted journals travelling the
same workflow with no fast path around the controls.

**Follow-ups.** "A contractor needs read-only access, except they prepare
reconciliations." "Permission to see an account versus post to it." "The approver is on
PTO." "The bill matches the PO. Can we skip the human review?"

**Common problems.** An `isAdmin` boolean. Filtering only in the client. A service
account that can read every tenant. Approval implemented by editing the live journal.
