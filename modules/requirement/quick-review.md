# Quick Review Mode

Use this mode for short requirement snippets, user stories, small optimizations, bug fixes, or quick pre-grooming checks.

## Output Shape
Keep the result concise. Prefer 4 sections:

### 1. Quick Classification
Classify the input as Bug Fix, Small Iteration, Optimization, or unclear. State whether the immediate problem and expected behavior are clear.

### 2. Top Requirement Gaps
List the most important unclear areas only. Prioritize gaps that affect testability, user-facing behavior, state transitions, or release validation.

Suggested table:

| Severity | Unclear Area | Clarification Question | Why It Matters | Owner |
|---|---|---|---|---|

### 3. Missing Acceptance Criteria
List 3-7 acceptance criteria or expected behaviors that should be added before implementation or testing.

### 4. Edge Cases to Test
List practical edge cases. Keep them grounded in the input and do not invent unrelated systems.

## Quick Review Rules
- Do not demand market analysis or competitor benchmarking for a small iteration unless the requirement itself depends on it.
- For bug fixes, focus on repro conditions, impacted users, expected vs actual behavior, regression scope, and verification strategy.
- If the input is too thin to review, ask for the missing minimum: user, current behavior, expected behavior, scope, and success criteria.
