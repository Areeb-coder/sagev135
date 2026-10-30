# Sage Antigravity Setup Pack


/goal

Build and continuously optimize the strongest possible Cambridge Battlecode Autumn 2026 bot, with the ultimate objective of achieving and maintaining the #1 leaderboard position. Starting with our modified Sage v135, develop an evidence-driven autonomous optimization pipeline that continuously scouts top competitors, analyzes official online match replays, identifies strategic weaknesses, implements superior strategies, and validates every improvement. Preserve the strongest validated bot at all times, prioritize winning over farming, and require my explicit approval before consequential changes, match queueing, uploads, or submission activation. Follow all project instructions in AGENTS.md.m

This ZIP contains the project instruction file and the two chat commands/prompts for setting up Antigravity.

## Files

- `AGENTS.md` — Persistent, detailed project instructions. Copy this file into the root of your existing `LockIN` repository:
  `E:\Projects\Bot\LockIN\AGENTS.md`
- `PLAN_PROMPT.txt` — Paste this into Antigravity chat first, using `/plan`. It requests a read-only audit and implementation plan.
- `GOAL_COMMAND.txt` — After reviewing the audit and approving the plan, paste this into Antigravity chat. It starts with `/goal` and defines the shorter persistent objective.
- `SETUP_ORDER.txt` — Quick setup sequence.

## Recommended order

1. Extract the ZIP.
2. Copy `AGENTS.md` into `E:\Projects\Bot\LockIN\`.
3. Open the LockIN repository/workspace in Antigravity.
4. Paste the contents of `PLAN_PROMPT.txt` into chat.
5. Review the read-only audit and implementation plan. Do not approve implementation until the baseline, SDK, match queue semantics, and safety plan are clear.
6. After you approve the plan, paste the contents of `GOAL_COMMAND.txt` into chat.
7. Keep human approval required for source modifications, match queueing, uploads, and activation as specified in the project instructions.

## Important

The reported Sage v135 Elo and exact current source/submission identity must be verified by the audit. The requested three-game diagnostic cycle is a hard limit: if the platform cannot guarantee exactly three total games, Antigravity must stop without queueing matches.

The pack does not contain or modify your bot source code. It contains project instructions and prompts only.
