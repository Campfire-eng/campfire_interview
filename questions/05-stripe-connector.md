# 5. Stripe: from webhook to native connector

| | |
| --- | --- |
| Track | Backend + integrations |
| Language | Python (sync worker), TypeScript (mapping UI contract) |
| Format | Pair for part one, design for part two |
| AI | **Off** |
| Time | 50 min |

**The problem, part one.** Stripe delivers `charge.succeeded` at least once. It has to
produce cash application and GL entries. Sketch `handle_webhook(payload, signature)`.

**The problem, part two.** Now make it one of the hundred-plus native integrations:
customers, invoices, payments, credit notes, products, with a mapping experience that a
controller can use on their own.

**Why we ask it.** Idempotency at the accounting boundary comes first. After that, we want
to see whether you treat sync as part of the product or as a background job that is
hidden from the user.

**What a strong answer covers.** Verifying the signature, a unique `(provider, event_id)`,
acknowledging only after persisting, periodic pull alongside webhooks, storing external
ids. Then the harder shape: an inbox for events and an outbox for posting, exactly one
journal per charge, replay safety, late refunds, out-of-order arrival when a payment
syncs before its invoice, cursors and backfill, mapping Stripe products to performance
obligations and GL accounts, rate limits, a dead-letter path with replay, and paused sync
made visible in the UI. Deeper still: a source-of-truth matrix (billing lives in Stripe,
books live in Campfire), partial payments, multiple Stripe accounts per entity, a
three-year backfill that does not overload the GL, a reconciliation job diffing Stripe's
list API against the inbox, contract tests against fixtures, and what the AI layer must
never do, such as posting against a charge id it invented.

**Follow-ups.** "The event was processed but posting failed after commit." "Stripe retried
mid-deploy." "They switched Stripe accounts." "An invoice was voided after we recognized
revenue."

**Common problems.** Posting to the GL with no unique key. Returning 500 on every retry.
Parsing JSON floats as dollars. Overwriting GL memos on every sync. Hardcoding the account
mapping.
