# Sage Cambridge Battlecode Autumn 2026 Optimization Project

Autonomous, evidence-driven optimization pipeline for the **Sage** Battlecode bot (`decrest` team, Team ID: `432f7d69-cce1-48c4-a446-2b293aa210b9`).

---

## Current Active Champion: **Sage v162**
- **Live Submission ID:** Version 162
- **Git Commit:** `add51ed` on branch `experiment/candidate-v67-improvements`
- **Benchmark Performance:** **28W – 14L (+8,782 net gems)** in 50-game symmetric validation
- **Milestone Tactical Breakthrough:** 
  - Overturned persistent map losses on open combat terrain: **Swept `00dunes` symmetrically (Side A: 977 vs 212, Side B: 705 vs 108)**.
  - Achieved project-record Gate 1 gem total (**18,490 gems, 18W – 6L**).
- **Core Innovations:**
  - **Carry-Priority Targeting Intelligence (`kill_value`):** Scaled target weighting to eliminate high-threat enemy carries first: Marcella (`1.45x`), Vesper Vale (`1.35x`), and Tavi (`1.20x`).
  - **Calibrated Squad Altar Cohesion:** `kHoldBonus = 2.25f` maintaining peak squad cohesion at contested objectives without over-committing to trivial gem detours.

---

## Validation & Promotion Architecture

The pipeline enforces a multi-dimensional, evidence-based evaluation model balancing statistical thresholds with broad strategic adaptability:

1. **Gate 1 (24-Game Fast Benchmark):**
   - 12 maps tested symmetrically (Side A and Side B, 24 games total) against `v67_baseline`.
   - Gate criteria: Must achieve $\ge 15\text{W}$ and positive net gem differential.
2. **Gate 2 (50-Game Statistical Benchmark):**
   - All 25 official maps tested symmetrically (Side A and Side B, 50 games total).
   - Gate criteria: Multi-dimensional evaluation assessing win count ($\ge 28\text{W}$), net gem generation ($>+8,500$ gems), and performance on historic loss maps (`00dunes`, `02crossing`, `01boss_battle`).
3. **Multi-Opponent Real Ladder Diagnostics:**
   - 30-game diagnostic batches (6 distinct match groups $\times$ 5 games) tested across ladder strata from Rank 20 to Rank 220+.
   - **Strict Diversity Guarantee:** Every match group is queued against a **strictly unique opponent** (no duplicate opponents per cycle).
   - Real-match telemetry analysis parses combat micro, itemization velocity, draft choices, and objective conversion to drive targeted strategic upgrades.

---

## Version History & Benchmark Results

| Version | Experiment | Key Changes / Strategic Hypothesis | Gate 1 (24g) | Gate 2 (50g Extended) | Multi-Opponent / Ladder Results | Status |
|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **v173** | **EXP-0136** | **Secured Banker Tribute Threshold:** Lowered kBankerCarry 20 -> 16 to bank sooner and eliminate repeated carrier deaths with large bags | **13W - 11L (-218)** | **29W - 13L (+10,140)** | Broke through the 28W plateau to 29W; record +10,140 net gems (+1,304 gem surge) | **ACTIVE CHAMPION** |
| **v171** | **EXP-0131** | **Gem-Carrier Bounty Interception (50 Ranked Losses Deep Dive):** Dynamic bounty multiplier (up to +60% kill priority on enemy carriers with gems) to intercept carriers before altars | **13W - 11L (-126)** | **28W - 14L (+8,836)** | Outright beat v170 (13W-11L); Gate 2 Net Gems improved (+8,836) | Superseded |
| **v170** | **EXP-0130** | **Ryth Priority Targeting (Ranked Loss Breakdown):** Scaled targeting for enemy Ryth (1.25x when carrying gems or <60% HP) to break frontline altar blockades | **13W - 11L (+1,582)** | **28W - 14L (+8,794)** | Outright beat v169 (+1,582 gems); 100% presence in ranked defeats | **PROMOTED** |
| **v169** | **EXP-0128** | **Varg Priority Execution (Ranked Analysis):** Elevated Varg cleave execution multiplier (1.25x -> 1.35x) to counter AoE melee carry attrition | **12W - 12L (0)** | **28W - 14L (+8,782)** | Ranked losses evidence: 100% presence in recent defeats | **PROMOTED** |
| **v168** | **EXP-0126** | **Tavi Area-Stun Priority Execution:** Scaled targeting for enemy Tavi (1.20x -> 1.35x) to eliminate disruptive area stuns | **12W - 12L (0)** | **28W - 14L (+8,782)** | Strategy X.0 Cycle 4 data: neutralizes high-focus stunner | **PROMOTED** |
| **v167** | **EXP-0125** | **Varg Cleave Priority Targeting:** Scaled execution weighting for enemy Varg (1.25x) to eliminate splash melee carries | **12W - 12L (0)** | **28W - 14L (+8,782)** | Strategy X.0 Cycle 3 data: 18.8% WR vulnerability countered | **PROMOTED** |
| **v166** | **EXP-0123** | **Prism Focus Priority Execution:** Scaled targeting for enemy Prism (1.25x) to neutralize gem-burst beam carry | **12W - 12L (0)** | **28W - 14L (+8,782)** | Strategy X.0 Cycle 2 data: 20.5% WR vulnerability addressed | **ACTIVE CHAMPION** |
| **v165** | **EXP-0122** | **Stellar Priority Execution:** Scaled targeting for enemy Stellar (1.30x) to eliminate long-range snipe carries | **12W - 12L (0)** | **28W - 14L (+8,782)** | Strategy X.0 Cycle 2 data: 19.4% WR vulnerability patched | **ACTIVE CHAMPION** |
| **v164** | **EXP-0120** | **Tactical Ranged Kiting:** Ranged units step back from adjacent melee threats when healthy to maintain range advantage | **12W - 12L (0)** | **28W - 14L (+8,782)** | **Sweeps 00dunes, 01boss_battle, 02crossing** | **ACTIVE CHAMPION** |
| **v163** | **EXP-0116b** | **Heart of Ruin Dynamic Targeting:** <45% HP 1.8x execution, >=45% HP 0.65x de-priority | **12W - 12L (0)** | **28W - 14L (+8,782)** | Strategy X.0 125-match diagnostic corpus | **Predecessor Champion** |
| **v162** | **EXP-0110** | **Combat Targeting Intelligence:** Weight high-threat carries (`Marcella 1.45x, Vesper 1.35x, Tavi 1.20x`) | **18W – 6L (+7,930)** | **28W – 14L (+8,782)** | **Sweeps `00dunes` symmetrically (977-212 & 705-108)** | **ACTIVE CHAMPION** 🏆 |
| **v161** | **EXP-0104** | **Altar Cohesion Calibration:** Fine-tuned `kHoldBonus = 2.25f` to break the gem accumulation ceiling | **18W – 6L (+7,168)** | **29W – 13L (+8,991)** | **Cycle 8: 7W – 23L** (5-0 sweep vs FürFortnite Rank 187, 2-3 vs geese geese go Rank 113) | **Fallback Champion** 🏆 |
| **v160** | **EXP-0085** | **Opportunistic Banking:** Detour to altar when `d <= 12 && gems >= 5` or `d <= 5` | **18W – 6L (+6,840)** | **29W – 13L (+8,589)** | Cycle 7: 11W - 19L (36.7% WR across 6 distinct opponents) | Superseded by v161 |
| **v159** | **EXP-0078** | **Sprint Banking:** Dynamic banking trigger when near victory threshold | **18W – 6L (+6,750)** | **28W – 14L (+8,992)** | Platform verified | Superseded by v160 |
| **v158** | **EXP-0075** | **Draft Adaptation:** 3v3 draft to `[Vesper, Marcella, Ryth]` | 17W – 7L (+5,786) | 28W – 14L (+8,863) | Cycle 5: 7W - 8L (46.7% WR vs peer/mid tiers) | Historic Baseline |
| **v157** | **EXP-0071** | Calibrate `kMaxTrips = 6.0f` (optimal camp round-trip siege threshold) | 19W – 5L (+6,979) | 30W – 12L (+10,035) | 4W - 6L vs Peer Rank 160 | Historic Baseline |
| **v135** | **Baseline** | Immutable protected reference baseline | 12W – 12L (0 gems) | 21W – 21L (0 gems) | Initial anchor | **PROTECTED BASELINE** |

---

## Recent Multi-Opponent Diagnostic Cycles

### Cycle 9 Diagnostics (30 Games vs 6 Strictly Unique Opponents)
Map Pool: `00dunes`, `01starfish`, `00split`, `02crossing`, `01the_farm`
- **Rank 217 Tier (`Midnight Altar Keepers`)**: **3W – 2L (60.0% WR)**
  - Won: `01the_farm` (1017 vs 336), `00split` (1010 vs 730), `00dunes` (1042 vs 442)
  - Narrow losses: `02crossing` (920 vs 1009), `01starfish` (326 vs 1008)
- **Rank 163 Tier (`Feral Monoliths`)**: **3W – 2L (60.0% WR)**
  - Won: `00split` (1000 vs 684), `01starfish` (1007 vs 279), `00dunes` (1031 vs 551)
  - Lost: `01the_farm` (654 vs 1023), `02crossing` (492 vs 1044)
- **Rank 130 Tier (`Kamikaze`)**: **1W – 4L (20.0% WR)**
  - Won: `02crossing` (1034 vs 650)
- **Rank 109 Tier (`Manta`)**: **2W – 3L (40.0% WR)**
  - Won: `01the_farm` (1099 vs 525), `00split` (1040 vs 681)
- **Rank 71 Tier (`cheesynachos`)**: **1W – 4L (20.0% WR)**
  - Won: `02crossing` (1019 vs 950)
- **Rank 60 Tier (`e1648263`)**: **0W – 5L (0.0% WR)**
- **Aggregate Cycle 9 Performance**: **10W – 20L (33.3% Win Rate)**
  - **Key Finding:** Reliable dominance on `00split` and `00dunes` across competitive brackets. Combat positioning on `02crossing` showed noticeable improvement.

### Cycle 8 Diagnostics (30 Games vs 6 Strictly Unique Opponents)
Map Pool: `00vault`, `01boss_battle`, `00quadrants`, `00split`, `02arena`
- **Rank 187 Tier (`FürFortnite`)**: **5W – 0L (100% Sweep!)**
  - Dominated all 5 maps: `02arena` (1000-252), `00split` (1185-347), `00quadrants` (1044-394), `01boss_battle` (1011-0), `00vault` (1045-4).
- **Rank 113 Tier (`geese geese go`)**: **2W – 3L (40.0% WR)**
  - Won: `00split` (1025 vs 712), `00vault` (1111 vs 897).
- **Ranks 20–154 (`DOOMSDAY`, `caterpillow`, `Rogue Lock Pickers`, `Rogue Gem Thieves`)**: Stalled on high-tempo itemization maps, highlighting the need for accelerated combat target prioritization.

---

## Experimental Hypotheses Tested (EXP-0086 to EXP-0110)

- **EXP-0110 (`kill_value` scaling on Marcella/Vesper/Tavi):** **PROMOTED (Sage v162)**. 18W-6L Gate 1 (+7,930 gems), 28W-14L Gate 2 (+8,782 gems). Unlocked symmetric sweep of `00dunes`.
- **EXP-0109 (`kFightBuild = false`):** Tested farming/earner item priority over durability. Result: 10W - 14L (-1,654 gems in Gate 1). Early durability is mandatory to survive camp damage and early enemy pressure. (*REJECTED*).
- **EXP-0108 (`kSiegeFrom = 400`):** Tested earlier monolith sieges. Result: 16W - 8L Gate 1, but caused early overcommitments on `01starfish` and `02fields`. (*REJECTED*).
- **EXP-0107 (Tightened `near_altar` to `d<=10 && gems>=10`):** Result: 16W - 8L Gate 1, but lost critical bank tempo on `02fields`. (*REJECTED*).
- **EXP-0106 (`kCarrierHuntGems = 50`):** Lowered altar defense carrier hunt threshold. Result: 17W - 7L Gate 1, 27W - 15L Gate 2 (+7,486 gems). Caused units to chase low-yield carriers away from camps. (*REJECTED*).
- **EXP-0105 (Earlier shop threshold at 150 gold):** Result: 13W - 11L in Gate 1. Excessive walking home interrupted early farming curves. (*REJECTED*).
- **EXP-0104 (`kHoldBonus = 2.25f`):** **PROMOTED (Sage v161)**. 18W-6L Gate 1 (18,152 gems), 29W-13L Gate 2 (+8,991 gems). Surpassed baseline gem threshold.
- **EXP-0103 (`kHoldBonus = 2.30f`):** Result: 18W-6L Gate 1, 28W-14L Gate 2 (+8,874 gems). Very close, inspired v161 calibration. (*REJECTED*).
- **EXP-0102 (`kTripShare = 0.45f`):** Result: 27W - 15L (+6,722 gems in Gate 2). Underestimated health cost per trip, leading to team wipes on camps. (*REJECTED*).
- **EXP-0101 (`kMaxTrips = 7.0f`):** Result: 27W - 15L (+7,600 gems in Gate 2). Over-extended squad into unviable late camp fights. (*REJECTED*).
- **EXP-0100 (`kCarryGems = 30`):** Result: 16W - 8L Gate 1, with severe regressions on `01boss_battle`. (*REJECTED*).
- **EXP-0099 (`kOpeningRounds = 110`):** Result: 29W - 13L (+7,792 gems in Gate 2). Fell short of champion net gem baseline. (*REJECTED*).
- **EXP-0098 (`kOpeningContested=0.40, kHoldBonus=2.5, kFieldBonus=3.6`):** Result: 29W - 13L (+7,853 gems in Gate 2). Plateaued below champion gems. (*REJECTED*).
- **EXP-0096 (`kHoldBonus = 2.5f`):** Result: 29W - 13L (+7,853 gems in Gate 2). (*REJECTED*).

---

## Repository Structure

```
├── bots/
│   ├── candidate_v67/        # Active development workspace (Sage v162)
│   ├── v67_baseline/         # Immutable local benchmark reference
│   ├── sagev135/             # Protected original baseline
│   └── sagev136/             # Experimental reference
├── run_candidate_benchmark.py# 24-game symmetric fast benchmark (Gate 1)
├── run_extended_benchmark.py # 50-game symmetric statistical benchmark (Gate 2)
├── queue_cycle9.py           # Automated diagnostic match group queueing script
├── track_cycle9.py           # Automated match monitoring and results tracker
├── run_cycle9_summary.py     # Deep match stats and telemetry analysis tool
└── README.md                 # Complete project documentation & benchmark history
```
