# FlowTreasury MVP

An AI-assisted treasury decision-support prototype built for a Product Manager application at **Zamp**.

**Live Demo**: https://flow-treasury-mvp--pranithamahib.replit.app  
**Case Study**: https://app.notion.com/p/FlowTreasury-Zamp-PM-Case-Study-3e8d93be68d381e9b80ac0eb41fa4acb?source=copy_link
**Demo**:https://www.loom.com/share/e5172f04ab344a978ea0a4b3201099e8

 ## Problem

Finance teams often have cash spread across multiple bank accounts but lack a simple way to
identify potential excess cash, understand upcoming liquidity needs, and decide how much
should remain liquid versus be allocated to a short-term, low-risk instrument.

 ## Target User

**Priya**, Finance Manager at a 150-person SaaS company. She manages cash across four bank
accounts, tracks expenses through spreadsheets, and wants visibility and confidence  not
another complicated finance system.

## What This Product Does

FlowTreasury helps a finance user go from **visibility → forecast → potential excess cash →
explainable recommendation → human approval → recorded action.**

1. **Overview** — total cash across all connected bank accounts, available liquidity, and
   upcoming obligations
2. **Forecast** — a 30-day view of expected outflows (payroll, vendors, taxes)
3. **Recommendation** — a suggested split between liquid cash and an illustrative short-term
   instrument, based on a configurable liquidity buffer
4. **Why this recommendation?** — a panel explaining the liquidity, safety, and opportunity
   reasoning behind the suggestion
5. **Confirmation** — the user can Accept, Modify, or Reject; the decision is recorded as an
   action (no real money moves)

## Key Product Decision: AI Recommends, Human Decides

This is **not** an autonomous investment tool. The AI surfaces potential excess cash and
explains its reasoning — the finance user always makes the final call. This was a deliberate
choice: financial actions are high-impact, and trust in fintech products comes from
explainability and human control, not automation.

## MVP Scope (MoSCoW)

| Priority | Feature |
|---|---|
| Must have | Cash dashboard, 30-day forecast, potential excess cash calculation, recommendation screen, Accept/Modify/Reject flow, action history |
| Should have | Reasoning/explanation panel, visible assumptions |
| Could have | Historical cash view, risk profile settings |
| Won't have (MVP) | Real bank integrations, real trading, autonomous money movement |

## Tech Stack

- Built with [Replit](https://replit.com) (AI-assisted / vibe-coding tool)
- Frontend: React
- Dummy/simulated data — no real bank connections

## What I Would Validate Next

- Do finance managers trust AI-generated allocation suggestions?
- What liquidity horizon do they actually use — 30, 60, or 90 days?
- What information needs to be visible before a recommendation can be approved?



All financial data shown is simulated — no real bank accounts, transactions, or investments
are involved.*
