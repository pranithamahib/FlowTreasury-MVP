# FlowTreasury

FlowTreasury is a simulated treasury decision-support workspace that helps finance teams understand cash, forecast liquidity, evaluate illustrative allocation recommendations, and record human decisions.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `artifacts/flowtreasury/src/App.tsx` — frontend routes, centralized demo state, calculations, and decision workflow.
- `artifacts/flowtreasury/src/index.css` — FlowTreasury visual system and responsive layout.
- `artifacts/flowtreasury/.replit-artifact/artifact.toml` — artifact routing and workflow metadata.

## Architecture decisions

- The first MVP is frontend-only with session-scoped simulated data; no bank, trading, or money-movement integrations are connected.
- Potential excess cash is derived from total account cash, expected obligations, and the editable liquidity buffer.
- Recommendation acceptance/rejection records an action locally and never executes a financial transaction.
- The review flow keeps allocation sums constrained to calculated potential excess and exposes the calculation before recording a decision.

## Product

- Overview of total cash, available liquidity, obligations, runway, and attention items.
- Cash position search/filter with account detail drawer.
- 30/60/90-day forecast views with upcoming obligations.
- Explainable recommendation, editable buffer and allocation, no-excess state, acceptance/rejection flow, and dynamic action history.
- Treasury settings for horizon, liquidity buffer, risk preference, and notifications.

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

_Populate as you build — sharp edges, "always run X before Y" rules._

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
