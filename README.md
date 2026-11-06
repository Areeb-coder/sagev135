# Sage v135 — Cambridge Battlecode 2026

A competitive autonomous bot for **Cambridge Battlecode Autumn 2026**, built around strategic decision-making, efficient resource collection, coordinated combat, and map-aware play.

> Developed and maintained by [Areeb Khalid](https://github.com/Areeb-coder).

## Competition Highlights

| Metric | Achievement |
|---|---:|
| **Peak leaderboard position** | **#129** |
| **Peak rating** | **1,828** |
| Competition | Cambridge Battlecode Autumn 2026 |
| Bot lineage | Sage v135 |

These are the bot's **peak achievements** during the competition, not a claim about its current live position or rating.

**Official team page:** [View Sage on the Cambridge Battlecode leaderboard](https://2026a.battlecode.co.uk/game/team/432f7d69-cce1-48c4-a446-2b293aa210b9)

## About the Bot

Sage v135 is an autonomous player designed for the Cambridge Battlecode 2026 strategy game. The project focuses on building a bot that can make strong decisions under the competition's per-turn constraints while balancing economic progress, map navigation, team coordination, and combat.

The strategic areas this bot is designed to address include:

- **Resource strategy:** collecting, carrying, and offering gems while balancing risk and reward.
- **Combat decision-making:** selecting engagements and targets with an emphasis on winning fights rather than blindly pursuing resource totals.
- **Pathfinding and navigation:** adapting movement to map geometry, obstacles, corridors, and changing battlefield conditions.
- **Coordination:** making individual units work toward coherent team-level objectives.
- **Efficiency:** keeping decision-making practical within the game engine's execution constraints.

The bullets above describe the project's strategic focus; they should not be read as a claim that every technique is implemented as a distinct subsystem in every build.

## Repository Contents

This repository currently contains the Sage v135 optimization/setup pack and its project instructions.

| Path | Purpose |
|---|---|
| `AGENTS.md` | Detailed instructions and guardrails for the optimization workflow |
| `PLAN_PROMPT.txt` | Read-only audit and planning prompt for Antigravity |
| `GOAL_COMMAND.txt` | Persistent optimization goal command |
| `SETUP_ORDER.txt` | Recommended setup sequence |
| `cambc.toml` | Cambridge Battlecode CLI project configuration |
| `bots/` | Bot-related project files |
| `sagev135/` | Sage v135 project directory |

## Optimization Approach

The project uses an evidence-driven improvement process:

1. **Establish a baseline** before changing strategy or implementation.
2. **Study match outcomes and replays** to identify recurring weaknesses and missed opportunities.
3. **Form a targeted hypothesis** for a strategic change rather than making arbitrary parameter adjustments.
4. **Benchmark against a consistent baseline** and inspect both aggregate results and map-specific regressions.
5. **Preserve the strongest validated version** so an experimental change does not replace a better-performing build without evidence.

The guiding principle is simple: **optimize for winning, not farming**. Resource collection matters when it contributes to winning the match.

## Getting Started

This repository includes the optimization workflow instructions. To use the pack:

1. Clone the repository:
   ```bash
   git clone https://github.com/Areeb-coder/sagev135.git
   cd sagev135
   ```
2. Review `AGENTS.md` and `SETUP_ORDER.txt`.
3. Follow the staged workflow in `PLAN_PROMPT.txt` before authorizing implementation.
4. Review the generated audit and confirm the local Cambridge Battlecode CLI / SDK setup before running or submitting a bot.

> **Important:** This repository's setup pack is not, by itself, a guarantee that a ready-to-submit bot binary or complete source build is present. Check the contents of `sagev135/` and `bots/` and validate the build with the competition CLI before submitting.

## Safety and Validation

- Keep a known-good version before experimenting.
- Validate changes with controlled matches and replay analysis.
- Check for regressions across different maps, not only aggregate win rate.
- Require explicit human approval before consequential source changes, match queueing, uploads, or submission activation.
- Do not queue a match batch unless its exact game count and platform behavior are understood.

## Links

- **GitHub repository:** [Areeb-coder/sagev135](https://github.com/Areeb-coder/sagev135)
- **Battlecode team page:** [Sage — Cambridge Battlecode 2026](https://2026a.battlecode.co.uk/game/team/432f7d69-cce1-48c4-a446-2b293aa210b9)
- **Competition:** [Cambridge Battlecode](https://battlecode.co.uk/)

---

*Peak results are historical highlights. Ratings and leaderboard positions can change over time; consult the official team page for live information.*
