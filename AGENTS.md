# AGENTS.md — Sage Cambridge Battlecode Optimization Project

## 1. Mission and project context

The project is located at:

`E:\Projects\Bot\LockIN`

The primary objective is to improve our modified Sage bot for Cambridge Battlecode Autumn 2026, targeting 1800+ Elo and stronger, repeatable competitive performance.

Current known context:
- Sage v135 is the current primary development baseline.
- Sage v135 is reported to be above 1700 Elo; verify this against actual leaderboard and match evidence.
- Sage v135 must be preserved as an immutable baseline.
- CPP21 is a secondary reference implementation, not the primary development target.
- Future experimental versions should be tracked separately (for example, Sage v136, v137, and onward).
- The strongest reliably validated version is the champion. Do not assume the newest version is the strongest.

Do not assume folder names, version labels, Elo claims, or submission identities are correct without verification.

## 2. Non-negotiable safety rules

### Initial audit
- Begin with a read-only audit.
- Do not modify source files, create or queue matches, upload submissions, activate submissions, delete files, or change the active submission during the initial audit.
- Present findings, uncertainties, blockers, and an implementation plan.
- Wait for explicit user approval before implementation.

### Protect the champion
- Never directly modify or overwrite the protected Sage v135 baseline.
- Preserve CPP21 and all existing bot versions.
- Use isolated branches, copies, or worktrees for experiments.
- Preserve Git history and record exact commits for every candidate.
- Keep a recoverable copy of the current champion and its submission package.
- Never delete previous submissions or experiment artifacts.

### Match restrictions
- Competitive diagnostic matches must be official online unranked matches.
- Do not run local gameplay matches.
- Do not run ranked matches.
- The requested diagnostic target is exactly three games total: one against each of the current top three opponents.
- Before queueing, verify the actual platform queue semantics and the exact number of games that will be created.
- If exactly three games cannot be guaranteed, STOP without queueing anything.
- In particular, if the platform queues groups of five per opponent, do not create fifteen games as a workaround.
- Never exceed the user's approved match count.
- Never invent opponent IDs, match IDs, replay files, submission IDs, or results.
- Collect all required replays and metadata before claiming that a diagnostic cycle is complete.

### Submission restrictions
- Building, packaging, uploading, and activating are separate operations.
- Never activate a new submission without explicit human approval.
- Do not change the active submission without explicit approval.
- Verify the platform response after every submission operation.
- Never claim an upload or activation succeeded without confirmation.

### Stop conditions
Stop safely if:
- Authentication fails.
- Queue semantics are ambiguous.
- The match count may exceed the limit.
- An opponent or submission identity cannot be verified.
- A required replay is missing.
- The build or package validation fails.
- The current champion cannot be protected or recovered.
- A platform operation behaves unexpectedly.

Do not bypass a safety rule to keep the process running.

## 3. Required initial repository audit

Inspect the complete repository without modifying it.

Verify and report:
1. Exact location and contents of Sage v135.
2. Git branch, commit, working-tree status, and relevant history.
3. All other Sage versions and experimental candidates.
4. Exact location and contents of CPP21.
5. Existing build system, compiler, SDK, and dependency requirements.
6. Current game rules and the actual current-season API.
7. Submission packaging requirements and expected directory structure.
8. Existing match, replay collection, parsing, analysis, and upload scripts.
9. Current active online submission, if verifiable.
10. Available leaderboard and opponent information.
11. Whether exactly three official unranked matches can be queued.
12. Missing components needed for the proposed pipeline.
13. Risks to the current champion, source tree, and active submission.

Do not move, rename, or reorganize existing source files during the audit.

The audit report must clearly separate:
- Verified facts.
- User-provided claims not yet verified.
- Inferences.
- Unknowns and blockers.

## 4. Strategic optimization priorities

Treat the following advice from higher-Elo competitors as high-priority hypotheses to investigate. Do not assume every recommendation is automatically beneficial; validate it against the current game's rules and replay evidence.

### A. Winning-oriented decision-making — critical priority

Investigate whether Sage overvalues farming, resource collection, or low-risk activity at the expense of winning.

Optimize for probability of winning, not raw resource accumulation.

Investigate:
- When farming is worthwhile.
- When to transition from farming to objective completion.
- Gem collection and tribute timing, where supported by the current game rules.
- Objective contesting and denial.
- Offensive timing.
- Defensive timing when ahead.
- Calculated aggression when behind.
- Converting a lead into a win.
- Avoiding unnecessary late-game farming when decisive progress is available.

A resource-rich losing position is not a successful strategy.

### B. Combat micro and targeting

Investigate and improve:
- Focused fire and coordinated target selection.
- Kiting and maintaining advantageous attack distance.
- Prioritizing tactically valuable eliminations.
- Threat evaluation using enemy health, damage, position, role, and strategic value.
- Avoiding wasted attacks on targets already likely to be eliminated.
- Fight, pursue, retreat, and regroup decisions.
- Preventing friendly units from entering engagements separately.
- Positioning that creates favourable engagements.

Do not blindly target the lowest-health enemy. Consider the tactical value and cost of each engagement.

### C. Inter-bot communication and coordination

Inspect the actual current SDK and game rules to determine what communication or shared-state mechanisms are supported.

If supported, investigate:
- Broadcasting enemy positions.
- Sharing recently observed enemy information.
- Team-wide focus fire.
- Target assignment.
- Preventing duplicate or conflicting objectives.
- Sharing danger and retreat information.
- Coordinating offensive and defensive movement.
- Handling stale, missing, or conflicting information.

If direct communication is unavailable, investigate only legitimate supported alternatives, such as shared state, common observations, or deterministic coordination. Never invent APIs or assume unsupported functionality.

### D. Pathfinding and map adaptation

Investigate:
- Bottleneck and corridor detection.
- Terrain-aware path costs.
- Threat-aware routing.
- Alternative routes around danger.
- Dynamic positioning.
- Team congestion and collision avoidance.
- Combat positioning.
- Map-specific objective access.
- Efficient path recalculation and caching.
- Cache invalidation when relevant map information changes.

The shortest route is not necessarily the best strategic route.

## 5. Research references

Study these repositories as sources of transferable ideas:

### Pantheon / previous-season winning implementation
https://github.com/HerbertTheBird/Cambridge-Battlecode

Study its postmortem and relevant source for:
- Dynamic action/state scoring.
- Reconsidering decisions from current observations.
- Efficient spatial representations.
- Threat-aware pathfinding.
- Intelligent unit allocation.
- Adaptive strategic decisions.

Important: this is a different season/game. Transfer architectural concepts only. Do not copy old-season mechanics, rules, or APIs into the current bot without verification.

### dpark2380 competitive development infrastructure
https://github.com/dpark2380/cambridge-battlecode

Study:
- Statistical regression gates.
- Opponent scouting.
- Experiment tracking.
- Online scrim workflows.
- Benchmarking.
- Version management.
- Rollback and non-regression practices.

### Local source of truth
- Sage v135 is the primary implementation to understand.
- CPP21 is a secondary reference.
- Other current-season sources may be investigated when reliable and relevant.

Do not blindly copy code. Explain why a proposed technique applies to the current game's actual rules and implementation.

## 6. Mandatory iterative improvement loop

Build a repeatable improvement system. Do not produce Sage v136 once and stop.

The required cycle is:

**SCOUT → COMPETE → COLLECT → ANALYZE → HYPOTHESIZE → EXPERIMENT → IMPLEMENT → VALIDATE → PROMOTE → REPEAT**

### Stage 1: Scout
- Identify the current top three leaderboard opponents.
- Verify team identities and submission information where available.
- Record the time and source of the leaderboard snapshot.
- Study available match histories and opponent tendencies.
- Do not silently substitute opponents if identities or submissions change.

### Stage 2: Official online diagnostics
- Target exactly three official online unranked games total.
- One game against each of the top three opponents.
- Verify our participating submission and each opponent's identity/version.
- Verify queue semantics and exact expected game count before submitting.
- If the platform cannot guarantee exactly three total games, stop without queueing.
- No local gameplay matches and no ranked matches.

### Stage 3: Collect
Collect and preserve:
- Match IDs and group IDs.
- Opponent identities and submission versions.
- Our participating submission identity.
- Map and side information.
- Results.
- Replay files.
- Game/engine version.
- Relevant logs and crash information.

Never overwrite previous replays. Mark a run incomplete if any required replay or metadata is missing.

### Stage 4: Analyze
Analyze every match individually and then collectively.

Investigate:
- Combat mistakes and targeting failures.
- Missed focus-fire opportunities.
- Kiting and engagement quality.
- Coordination failures.
- Pathfinding, bottlenecks, and positioning.
- Farming inefficiency and missed objectives.
- Objective timing and victory conversion.
- Opponent-specific and map-specific weaknesses.

Separate repeated weaknesses from isolated incidents. Use only metrics supported by actual replay data. Explicitly mark unavailable metrics rather than estimating them.

### Stage 5: Hypothesize
For each proposed experiment, document:
- Unique experiment ID.
- Observed weakness.
- Replay evidence.
- Proposed change.
- Expected benefit.
- Computational/fuel cost.
- Regression risk.
- Success metrics.
- Files likely to change.

### Stage 6: Select and implement
- Select the highest-value evidence-backed experiment.
- Change one primary strategic hypothesis per experiment.
- Work on an isolated branch/copy.
- Preserve the current champion.
- Start with Sage v136 only after the audit and approval.

### Stage 7: Validate
Perform approved non-gameplay checks such as:
- C++ compilation.
- Static analysis and correctness checks.
- Legal-action and bounds checks where testable without running a game.
- Package structure and size checks.
- Computational/fuel profiling if available without local gameplay.
- Review of changed files.
- Regression checks against available historical evidence.

Do not run local gameplay matches.

Competitive validation must use approved official online unranked matches and must obey the exact match cap. Do not automatically run another batch if the current three-match cap has already been used; request approval for a new diagnostic cycle.

### Stage 8: Decision
Classify each candidate:
- PASS: satisfies configured evidence and safety criteria.
- REJECT: fails or introduces unacceptable regressions.
- INCONCLUSIVE: insufficient evidence.

Do not promote based on one lucky win, a small noisy Elo fluctuation, or a single isolated replay.

### Stage 9: Promote and repeat
- Prepare a candidate for promotion only after it passes.
- Require explicit human approval before activation.
- Preserve the prior champion and rollback package.
- Record the decision and begin the next cycle using the strongest validated champion.
- If no meaningful improvement is supported, keep the champion unchanged.

## 7. Experiment management

Maintain a permanent experiment backlog and history.

Example:

**EXP-0001 — Win-oriented utility function**

Hypothesis: Sage spends too many turns farming when decisive objective progress is available.

Evidence: Cite exact replay segments showing inefficient resource collection or missed objective opportunities.

Change: Adjust strategic scoring to account for victory probability, objective urgency, remaining time, resources, and relative team strength, subject to actual game rules.

Metrics: Win outcomes, objective timing, gems collected/tributed if available, late-game farming time, and relevant combat/objective measures.

Every experiment must record:
- ID and date.
- Baseline commit.
- Candidate commit.
- Hypothesis and evidence.
- Changed files.
- Build/check results.
- Match IDs and replay references, if any.
- Metrics and limitations.
- PASS/REJECT/INCONCLUSIVE decision.
- Human approval and promotion status.

Learn from failed experiments. Do not repeat a completed experiment without a documented reason.

## 8. Regression gate and champion protection

Use the experimental methodology from dpark2380 where applicable.

The gate should consider:
- Build success.
- Correctness and runtime-safety evidence.
- Submission validity.
- Strategic target metrics.
- Non-regression on protected metrics.
- Computational cost.
- Quality and quantity of evidence.

Do not claim statistical significance when the sample size does not support it. Three diagnostic games are useful for targeted qualitative diagnosis but are not sufficient by themselves to prove a small win-rate improvement.

Maintain:
- Protected Sage v135.
- Current validated champion.
- Experimental candidates.
- Git commits and branches.
- Match and replay history.
- Experiment reports.
- Rollback packages.
- Promotion history.

## 9. Submission safety

Keep these separate:
1. Build.
2. Package.
3. Upload.
4. Activate.

Never activate a candidate without explicit human approval. Never change the active submission without approval. Verify every platform response and do not claim success without confirmation.

## 10. Required reporting

After the initial audit, provide:
1. Repository inventory.
2. Verified bot/version map.
3. Sage v135 architecture report.
4. CPP21 reference summary.
5. SDK/API capability report.
6. Competitive evidence and uncertainties.
7. Strategic weakness assessment.
8. Combat improvement design.
9. Communication design.
10. Pathfinding/map adaptation design.
11. Winning-oriented decision design.
12. Iterative pipeline architecture.
13. Implementation roadmap and dependencies.
14. Safety risks and blockers.

After each approved improvement cycle, report:
- Previous champion and candidate.
- Opponents and verified submission versions.
- Exact match count and match IDs.
- Replay collection status.
- Individual and aggregate findings.
- Experiment hypothesis and modified files.
- Build and validation results.
- PASS/REJECT/INCONCLUSIVE decision.
- Upload/activation status.
- Current champion and rollback status.
- Next recommended experiment.

## 11. Operating principle

The objective is not more code, more complicated algorithms, or higher version numbers.

The objective is measurable improvement in actual competitive performance: better decisions, more favourable engagements, effective coordination, smarter movement, stronger objective play, and more wins against strong opponents.

Always prioritize verified evidence, current-season rules, preservation of the strongest bot, and explicit user approval for consequential actions.
