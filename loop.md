# Suggested loop

Keep the domain constant (books must balance, close must lock, AI must be reviewable). Vary *how* you observe the candidate.

## Recruiter / hiring manager (30 min)

Accounting curiosity, empathy for controllers rather than consumers, comfort with in-office SF collaboration. Not ASC 606 trivia.

## Technical screen (60 min) — one AI-off coding exercise

| Screening for | Use |
| --- | --- |
| Backend / full-stack | Q1 journal posting (Python) or Q2 trial balance (TypeScript) |
| Product-leaning full-stack | Q10 period close (TypeScript) |
| Data / AI | Q7 bank matching (Python), kept AI-off for the screen |

Shared editor, tests already in the repo, no AI. Watch for invariants, naming, and what they ask before typing.

## Onsite, four sessions of 45–50 min

1. **Hands-on with AI allowed** — Q7 matching, Q17 model evaluation, Q16 amortization, or Q11 flux. Grade whether they verify the books, not whether the first draft compiled.
2. **Schema and backend, AI-off** — Q3 GL schema, then Q5 Stripe ingestion or Q8 ASC 606.
3. **System design, AI-off** — Q4 consolidation, Q9 multi-currency, or Q18 continuous close.
4. **Product or AI trust** — Q6 review queue, Q12 recon workspace, Q13 Ember grounding, or Q19 model feedback loop.

Swap in Q14 (permissions, segregation of duties, approvals) for platform or security-leaning roles. Swap in Q20 (audit and point-in-time) when the role touches reporting or compliance.

## Track-specific onsite mixes

| Role | Sessions |
| --- | --- |
| Full-stack product | Q2 or Q10 hands-on, Q3 schema, Q6 review queue, Q12 recon workspace |
| Backend / platform | Q1 hands-on, Q3 schema, Q5 Stripe, Q14 permissions and approvals |
| Data engineering | Q7 hands-on, Q11 flux, Q15 duplicates, Q20 audit and point-in-time |
| AI engineering | Q17 hands-on eval, Q13 Ember grounding, Q19 feedback loop, plus Q1 AI-off to prove they can hold the ledger invariant |

The AI-engineering loop deliberately includes one AI-off ledger exercise. Someone shipping autonomous accounting must understand double-entry without a model's help.

## Take-home (optional, 3–4 hours)

Q7, Q11, Q16, or Q17. Explicitly allow AI. Require a short write-up covering invariants, failure modes, and what they would refuse to automate. Reject submissions with no tests and no mention of audit trail.

## What not to do

- Don't add graph or dynamic-programming puzzles "to see if they're smart."
- Don't pass someone who designs an elegant event bus that can post unbalanced journals.
- Don't pass an AI candidate whose evaluation story is a single accuracy number.
- Don't fail a strong junior for missing intercompany elimination on the first prompt — that's a senior follow-up.
