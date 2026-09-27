---
name: Conflicting demo metrics
description: How to handle product briefs whose headline demo metric conflicts with detailed sample rows.
---

When a product brief gives a named headline KPI and granular sample values that do not reconcile, preserve the headline KPI as an explicit shared state value and keep the granular rows for their own views.

**Why:** Demo briefs are often authored from separate product and data examples; silently recalculating the headline can make the shipped experience contradict the requested acceptance criteria.

**How to apply:** Treat the explicitly named KPI as the source of truth for the surface where it is specified, avoid hiding the discrepancy, and keep all user-editable calculations derived from the shared state model.