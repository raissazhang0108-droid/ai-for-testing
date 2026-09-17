# Full Review Mode

Use this mode for PRDs, epics, major features, release-critical flows, incentive/financial mechanics, user lifecycle changes, analytics-heavy features, or when the user asks for a complete QA/Test Architect review.

## Output Shape
Use the sections below, but skip or compress categories that are clearly irrelevant. Lead with critical risks when present.

### 1. Requirement Scale & Context Evaluation
Classify the input as Epic, Major Feature, Small Iteration, Optimization, or Bug Fix. Explain whether the context is sufficient for that scale.

For Major Features or Epics, check whether the business rationale is justified by at least one of: user feedback, business goal, market trend, competitor benchmark, operational pain point, or platform/technical need.

For smaller changes, focus on whether the immediate problem statement and user pain point are clear.

### 2. Business Value & Success Metrics
Assess whether the requirement defines a clear objective. Look for relevant value drivers:
- Direct business metrics: conversion rate, GMV, sign-ups, activation, revenue, order volume.
- User experience metrics: retention, churn reduction, CSAT, completion rate, drop-off reduction.
- Technical/platform metrics: scalability, reliability, operational efficiency, reuse, data quality.

Flag vague claims such as “improve user experience” or “make the system better” when there is no measurable success criterion or observable acceptance criterion.

### 3. Ambiguities & Vague Terms
List vague words, undefined concepts, or unclear statements. Examples: “new user,” “eligible,” “fast,” “real time,” “successful,” “active,” “high priority,” “limited time,” “normal user.”

### 4. Missing Acceptance Criteria
Identify missing happy paths, negative paths, validation rules, error states, permissions, eligibility rules, state transitions, and expected UI/API behavior.

### 5. Edge Cases & Boundary Risks
Identify unusual user behaviors, data boundaries, concurrent actions, retry flows, expired states, network failures, duplicate submissions, race conditions, localization, empty states, and long-text display issues.

### 6. Historical Data Integrity & Backward Compatibility
Apply this section when the requirement changes existing data, schemas, user account states, active coupons/subscriptions/orders, or existing workflows.

Check whether the PRD defines:
- Data migration or backfill rules.
- Behavior for legacy users or existing records.
- Behavior for in-flight transactions or active states during deployment.
- Rollback or compatibility expectations.

### 7. Performance & Scalability Risks
Apply this section for high-concurrency flows, batch jobs, heavy queries, media-heavy frontend pages, flash sales, coupon claims, or notification bursts.

Look for explicit non-functional requirements such as peak QPS/TPS, latency SLA, rate limits, async processing, queueing, caching, retry rules, or degradation behavior.

### 8. Security, Fraud & Compliance
Apply this section for user data, authentication, payments, coupons, refunds, incentives, external APIs, sensitive data, or abuse-prone workflows.

Look for missing constraints around fraud, farming, brute force, replay, malicious concurrent requests, rate limits, PII masking, secure tokens, permission boundaries, and auditability.

### 9. Data Tracking & Observability
Apply this section for user-facing flows, conversion funnels, engagement metrics, and business goals.

Check whether the PRD defines event names, trigger timing, event properties, funnel definitions, error logging, monitoring rules, dashboards, or validation methods for success metrics.

Flag a mismatch when business goals are stated but tracking requirements are missing.

### 10. UI/UX Consistency & Accessibility
Apply this section for client-facing web/mobile flows.

Check for loading states, empty states, error messages, timeout behavior, disabled button states, confirmation dialogs, long translations, responsive layout, accessibility labels, and fallback behavior.

### 11. Cross-Feature Conflicts
Identify conflicts with existing product behavior, permissions, analytics, business rules, security constraints, data models, or other active features.

### 12. Clarifying Questions
Provide a prioritized list of questions for the next sprint refinement, grooming, or requirement review.

Phrase questions in collaborative American workplace English. Prefer wording such as:
- “Could we clarify the expected behavior when...?”
- “Just to make sure we test this correctly, should...?”
- “Do we have a success metric for...?”
- “Who should own the decision on...?”

### 13. Cross-Functional Ownership Matrix
For each important item, provide a table:

| Severity | Unclear Area | Clarification Question | Why It Matters for QA | Suggested Owner |
|---|---|---|---|---|

## Full Review Rules
- Do not fill every section just to satisfy the checklist. If a category is not relevant, skip it or state “No major concern based on the provided text.”
- If the requirement involves financial incentives, coupons, rewards, refunds, payments, user identity, or abuse-prone mechanics, pay special attention to fraud, concurrency, eligibility, state transitions, rollback, and observability.
- If the requirement changes existing states or active records, always check backward compatibility and in-flight behavior.
