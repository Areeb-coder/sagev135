# Sage Cambridge Battlecode Autumn 2026 Optimization Project

Autonomous, evidence-driven optimization pipeline for the **Sage** Battlecode bot (`decrest` team, Team ID: `432f7d69-cce1-48c4-a446-2b293aa210b9`).

---

## Current Active Champion: **Sage v160**
- **Live Submission ID:** Version 158
- **Git Commit:** 8cef948 on branch experiment/candidate-v67-improvements
- **Peak Performance:** **28W – 14L (+8,863 net gems)** | **40% WR vs Peer Rank 160 (2W-3L, 100% win on starfish & fields)**

---

## Validation & Promotion Architecture

The pipeline enforces a strict, two-gate statistical non-regression model:

1. **Gate 1 (24-Game Fast Benchmark):**
   - 12 maps tested symmetrically (Side A and Side B, 24 games total) against `v67_baseline`.
   - Gate criteria: Must achieve $\ge 15\text{W}$ and positive net gems.
2. **Gate 2 (50-Game Statistical Benchmark — Sole Promotion Gate):**
   - All 25 official maps tested symmetrically (Side A and Side B, 50 games total).
   - Gate criteria: Must strictly surpass the historical peak net gem record of the champion bot.
3. **Telemetry & Real Ladder Match Diagnostics:**
   - 20 games official unranked diagnostic batch:
     - 15 games (3 groups $\times$ 5 games) vs Top 3 leaderboard opponents: Rank 1 (`Intercontinental Fish`), Rank 2 (`prism best girl`), Rank 3 (`Mite`).
     - 5 games (1 group $\times$ 5 games) vs peer opponent (~+20 ranks, `HighCortisol` ~Rank 160).
   - Continuous parsing and analysis of the 15 most recent ranked losses to address real competitive meta challenges.

---

## Version History & Benchmark Results

| Version | Experiment | Key Changes / Strategic Hypothesis | Gate 1 (24g) | Gate 2 (50g Extended) | Official Match Results | Status |
|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **v158** | **EXP-0075** | Adapt 3v3 draft to [Vesper, Marcella, Ryth] to secure front-line CC | 17W - 7L (+5,786) | 28W - 14L (+8,863) | **2W - 3L vs Rank 160 cronjohn** (wins starfish & fields) | **ACTIVE CHAMPION** 🏆 |
| **v157** | **EXP-0071** | Calibrate kMaxTrips = 6.0f (optimal camp round-trip siege threshold, broke +10k net gems!) | **19W - 5L** (+6,979 gems) | **30W - 12L (+10,035 gems)** | **4-6 (40% WR vs Peer Rank 160)**: Won 01starfish & 02fields symmetrically | **Fallback Champion Baseline** 🏆 |
| **v156** | **EXP-0070** | Calibrate kMaxTrips = 5.5f (further relaxed siege round-trip limit for complex maps) | **19W - 5L** (+6,884 gems) | **30W - 12L (+9,940 gems)** | Active on platform | **Superseded by v157** 🏆 |
| **v155** | **EXP-0066** | Calibrate kMaxTrips = 5.0f (further expanded camp round-trip ceiling for sieges) | **19W - 5L** (+7,278 gems) | **30W - 12L (+9,884 gems)** | Active on platform | **Superseded by v156** 🏆 |
| **v154** | **EXP-0058** | Calibrate kMaxTrips = 4.5f (allow more camp round-trips before declaring unreachable siege) | **19W - 5L** (+7,318 gems) | **29W - 13L (+9,808 gems)** | Superseded by v155 | Baseline |
| **v153** | **EXP-0047** | Calibrate kTripShare = 0.50f (higher squad fight sustain before retreat) | **19W – 5L** (+6,945 gems) | **29W – 13L (+9,735 gems)** | Queueing next cycle | **Superseded** 👑 |
| **v152** | **EXP-0043** | Calibrate kHoldBonus = 2.2f (peak contested altar priority & defensive grouping) | **19W – 5L** (+7,075 gems) | **30W – 12L (+9,685 gems)** | Queueing next cycle | Promoted -> Superseded |
| **v151** | **EXP-0039** | Calibrate `kHoldBonus = 2.0f` (tighter squad grouping at contested altars) | **18W – 6L** (+6,680 gems) | **29W – 13L (+9,611 gems)** | Queueing next cycle | Promoted -> Superseded |
| **v150** | **EXP-0036** | Tune `kHoldBonus = 1.8f` (from 1.5f) to prevent enemy tributes | **18W – 6L** (+6,482 gems) | **29W – 13L (+9,355 gems)** | 1-4 vs HighCortisol (1037-73 on starfish) | Promoted -> Superseded |
| **v149** | **EXP-0029** | Calibrate `kCarryGems = 35` (down from 40; optimal trip tempo) | **17W – 7L** (+6,330 gems) | **28W – 14L (+8,555 gems)** | 4-1 vs Gilded Gold (Rank 161) | Promoted -> Superseded |
| **v148** | **EXP-0015** | `kSoloDangerRounds = 10` (from 15; faster solo farming re-entry) | **17W – 7L** (+6,048 gems) | **27W – 15L (+7,036 gems)** | 5-0 vs Rank 162 | Promoted -> Superseded |
| **v147** | **EXP-0013** | `kSoloDangerRounds = 15` (from 20) | **17W – 7L** (+5,890 gems) | **26W – 16L (+6,889 gems)** | 3-2 vs Rank 165 | Promoted -> Superseded |
| **v146** | **EXP-0012** | `kSoloDangerRounds = 20` (from 30) | **16W – 8L** (+5,210 gems) | **27W – 15L (+6,651 gems)** | N/A | Promoted -> Superseded |
| **v145** | **EXP-0011** | `kSoloDangerRounds = 30` (from 40) | **16W – 8L** (+4,980 gems) | **26W – 16L (+6,676 gems)** | N/A | Promoted -> Superseded |
| **v144** | **EXP-0010** | Calibrated solo horizon, bag size and dash threshold | **16W – 8L** (+4,800 gems) | **26W – 16L (+6,480 gems)** | N/A | Promoted -> Superseded |
| **v143** | **EXP-0008** | Validated `kWaitBank = true` and `kWaitBankMin = 5` | **15W – 9L** (+4,100 gems) | **25W – 17L (+5,800 gems)** | N/A | Promoted -> Superseded |
| **v142** | **EXP-0002** | Base `candidate_v67` upgrade over v65 | **15W – 9L** (+3,800 gems) | **25W – 17L (+5,400 gems)** | 3-2 vs Rank 170 | Promoted -> Superseded |
| **v135** | **Baseline** | Immutable protected reference baseline (v65) | 12W – 12L (0 gems) | 21W – 21L (0 net gems) | Initial anchor | **PROTECTED BASELINE** |

---

## Key Experimental Hypotheses Tested (Rejected or Inconclusive)

- **EXP-0038 (`kWillowSmall = true` in 4v4/3v4):** Tested Willow over Tavi in 4v4 formats. Result: 27W – 15L (+7,846 gems), regressed from champion peak. Tavi's remote shopping ability provides superior tempo on small maps. (*REJECTED*).
- **EXP-0037 (`kTripShare = 0.40f`):** Tested lower trip health tolerance for camp farming. Result: 28W – 14L (+7,439 gems), caused excessive camp resetting. (*REJECTED*).
- **EXP-0035 (`kDeathStep = 0.15f`):** Tested higher retreat caution on teammate death. Result: 16W – 8L (+3,871 gems in Gate 1). (*REJECTED*).
- **EXP-0034 (`kStallRounds = 45`):** Reduced camp stall timeout. Result: 14W – 10L (+4,360 gems in Gate 1). (*REJECTED*).
- **EXP-0033 (`kDashKill = 2.5f`):** More aggressive dash targeting threshold. Result: 26W – 16L (+6,936 gems in Gate 2). (*REJECTED*).
- **EXP-0032 (`kCarryGems = 30`):** Tested lower carry gem threshold. Result: 15W – 9L (+3,583 gems in Gate 1); caused excessive altar transit overhead. (*REJECTED*).
- **EXP-0031 (4v4 draft Vendetta 4th pick):** Regressed early 4v4 combat. (*REJECTED*).
- **EXP-0030 (Treasure Shard priority for Vesper):** Result: 27W – 15L (+6,236 gems in Gate 2). (*REJECTED*).
- **EXP-0026 (`kGoldWeight = 0.20f`):** Failed Gate 1 (13W – 11L). (*REJECTED*).
- **EXP-0024 (5v5 Tavi over Willow):** Failed Gate 1 (14W – 10L). (*REJECTED*).
- **EXP-0023 (`kHurtFlee = true`):** Failed Gate 1 (13W – 11L). (*REJECTED*).

---

## Insights from Real Match Diagnostics

### 1. Match Diagnostics vs Peer (~Rank 160: `HighCortisol`)
- **Dominant Win on `01starfish` (1,037 vs 73 gems):** Marcella dominated combat (22 kills, 2 deaths, 36k damage), enabling uncontested early tributes.
- **Narrow Losses on `00lanes` (954 vs 1,002 gems) & `02fields` (908 vs 1,133 gems):**
  - Our squad had superior combat stats (e.g. Marcella 9k damage, zero deaths), but the opponent achieved faster split-second altar drops.
  - Inspired **EXP-0036 & EXP-0039 (`kHoldBonus = 1.8f -> 2.0f`)**, directly rewarding squads for staying grouped near altars to contest and intercept opponent tributes.

### 2. Match Diagnostics vs Top 3 Opponents (`Intercontinental Fish`, `prism best girl`, `Mite`)
- **Combat Burst Meta:** Top competitors aggressively draft **Focus-scaling burst items** and coordinate instant focus fire when engaging our squads.
- **Camp Denial:** Top 1 (`Intercontinental Fish`) invades our side early on 5v5 maps (`02guardians`, `00quadrants`, `02tangle`) to eliminate monster camps before our squad arrives.
- **Draft Consistency:** Top teams almost universally prioritize `[Marcella, Vesper Vale, Vendetta/Ryth]`. Our core 5v5 draft `[Vendetta, Vesper Vale, Ryth, Willow, Marcella]` remains the highest local performer.

---

## Repository Structure

```
├── bots/
│   ├── candidate_v67/        # Active development workspace (v151)
│   ├── v67_baseline/         # Immutable local benchmark reference
│   ├── sagev135/             # Protected original baseline
│   └── sagev136/             # Experimental reference
├── run_candidate_benchmark.py# 24-game symmetric fast benchmark (Gate 1)
├── run_extended_benchmark.py # 50-game symmetric statistical benchmark (Gate 2)
├── queue_v150_diagnostics.py # Automated online match group queueing script
├── track_v150_diagnostics.py # Automated online match monitoring and results parser
└── README.md                 # Project documentation & benchmark history
```


### Cycle 5 Multi-Opponent Evaluation (Sage v160 - Active Champion)
Tested across 3 distinct tiers with strict 1-match-group-per-opponent constraint:
- **Peer Tier (Rank 171 - FBOT5)**: **4W - 1L (80.0% Win Rate)**
  - Won: `00lanes` (1004 vs 950), `01islands` (1000 vs 840), `02gift_wrapping` (1008 vs 998), `00gemfight` (1033 vs 178)
  - Lost: `01the_farm` (542 vs 1020)
- **Mid Tier (Rank 98 - deadlock worst game ever)**: **3W - 2L (60.0% Win Rate)**
  - Won: `00lanes` (1008 vs 797), `02gift_wrapping` (1078 vs 865), `00gemfight` (1006 vs 200)
  - Lost: `01the_farm` (329 vs 1024), `01islands` (764 vs 1007)
- **Top Tier (Rank 4 - Ad Astra)**: **0W - 5L (0.0% Win Rate)**
- **Aggregate Win Rate**: **7W - 8L (46.7%)** — *highest multi-opponent diversity win rate achieved to date*.
