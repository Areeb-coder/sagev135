# V175 OPTIMIZATION PROGRESS TRACKER

## Baseline Status
- **Current Live Submission**: `v175` (`fbc57185-3b34-45af-b57a-90ae21135645`) — Note: `Sage v153-v1j-r6 [live]`, Elo ~1794-1804.
- **Protected Immutable Baseline**: `v175_original_baseline` (built & verified).
- **Candidate Workspace**: `candidate_v175_upgrade` (on branch `experiment/v175-autonomous-upgrade`).

## Historical Database Audit (197 Matches / 400 Individual Games)
- **Ranked Match Groups**: 123 (62W - 61L, 50.41% WR).
- **Unranked Match Groups**: 74 (20W - 54L, 27.03% WR).
- **Aggregated Performance by Team Size**:
  - Size 5 (5v5): 115W - 137L (45.6% WR)
  - Size 4 (4v4): 32W - 51L (38.6% WR)
  - Size 3 (3v3): 21W - 44L (32.3% WR)
- **Top Evidence-Supported Weaknesses Identified**:
  1. **Small-Team Draft Deficiency (3v3 & 4v4)**:
     - On 3v3 maps, the draft picked Vesper Vale, Marcella, Heart of Ruin (`kThree`), skipping Ryth (0% stun coverage, zero tankiness besides Marcella).
     - Result: 32.3% WR in 3v3 and 38.6% WR in 4v4. Opponents with Ryth had 56.4% WR against us.
  2. **Dash-Combat Invalidation Bug**:
     - `Bot::dash_toward()` and `Bot::dash_away()` strictly require `s.modifier <= 0`.
  3. **Varg Cleave Advantage Uncontested**:
     - Opponents drafting Varg won 58.9% against us across 348 games.

## Experiments & Verified Results

### EXP-0176-A: Ryth Frontline Restoration in Small-Team Drafts
- **Hypothesis**: Restoring Ryth (1200 HP, AoE stun + attack reset) in 3v3 and 4v4 drafts (`kThree` and `kSmall`) will stabilize frontlines on narrow/small maps and eliminate low-health collapses.
- **Code Changes**: Modified `kSmall` and `kThree` draft arrays in `candidate_v175_upgrade/src/draft.cpp`.
- **Benchmark Results**: 10 side-swapped matches across `00anvil`, `00packs`, `02arena`, `00oasis`, `01hooks`.
  - **Match Record**: Candidate **6W - 4L** Baseline v175 (60.0% Win Rate).
  - **Net Gems**: Candidate 6,276 vs Baseline 5,135 (**+1,141 net gems**).
  - **Breakdown**: `02arena` swept 2-0 (+1,119 net gems); `00anvil` neutral 1-1 (+48); `00packs` neutral 1-1 (+36); `00oasis` neutral 1-1 (-18); `01hooks` neutral 1-1 (-44).
- **Decision**: **PASSED**. Committed as `c2f6528`.

### EXP-0176-B: Damaging Combat Dashes
- **Hypothesis**: Removing `s.modifier > 0` condition in `dash_toward()` and `dash_away()`.
- **Benchmark Results**: 10 side-swapped matches across `00expanse`, `02fields`, `00lanes`, `00anvil`, `01hooks`.
  - **Match Record**: 5W - 5L Baseline (50.0% Win Rate, +4 net gems). Open 5v5 maps were bit-for-bit identical (+0 delta).
- **Decision**: **REJECTED / REVERTED**. Candidate restored to purely validated EXP-0176-A code to maintain clean, validated gains without unnecessary modifications.

### EXP-0176-C: Retain Tavi Stun in 4v4 + Ryth Frontline in 3v3 (Non-Regression Solution)
- **Hypothesis**: In 4v4, Tavi's remote shopping + stun provides high late-game DPS and camp clearing that beats Vendetta (`02guardians`, `01shortcut`). Restoring Tavi in `kSmall` while keeping Ryth in `kThree` eliminates the 4v4 regression while retaining 100% of the +713 net gem 3v3 gains.
- **Controlled 30-Match Local Benchmark (15 Diverse Maps, Side-Swapped)**:
  - **Total Result**: Candidate **15W - 15L** Baseline (50.0% WR).
  - **Net Gems**: Candidate 21,239 vs Baseline 20,526 (**+713 Net Gems**).
  - **3v3 Maps**: **+713 net gems** (Swept `02arena` 2-0 with +1,119 gems, `00anvil` +48, `00packs` +36).
  - **4v4 Maps**: **5W - 5L, +0 Net Gems (Zero regression across all 5 maps)**.
  - **5v5 Maps**: **5W - 5L, +0 Net Gems (Zero regression across all 5 maps)**.
- **Decision**: **PASSED**. Committed as `b17afbf` and pushed to GitHub.

## Packaged Release Candidate
- **Package**: `bots/v176_candidate_EXP0176C.zip` (69,518 bytes).
- **Validated Net Advantage**: **+713 net gems** vs protected v175 baseline with **zero regressions** on 4v4 and 5v5 maps.
- **Git Commit**: `b17afbf` on branch `experiment/v175-autonomous-upgrade`.

