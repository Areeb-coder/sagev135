# Final Release Package: Sage V153 (v1j-r6)
Release Date: 2026-11-02
Baseline: v1j_r6_checkpoint (Derived from Champion v2 / Candidate v1i)

## 1. Verified Improvements Included
1. **EXP-0029 Map-Aware Altar Guard (`altars.size() <= 2`)**:
   - Gated early altar detours specifically on single/dual-altar maps (`00ribs`, `01hooks`).
   - Prevents premature, low-gem (6-9 gem) detachments on crowded maps.
   - Result: 11-9 (55% WR) in 20-match general benchmark; converts `00ribs` and `01hooks` from 0-2 losses to 1-1 neutral.
2. **Four Target Regression Maps Preserved**:
   - `00ribs`: Preserved 1-1 neutral (+0 delta).
   - `01hooks`: Preserved 1-1 neutral (+0 delta).
   - `02gift-wrapping`: Preserved 1-1 neutral (+0 delta).
   - `01yellow-brick-road`: Preserved baseline behaviour (Candidate v1m's corridor gate rejected to prevent Side A regression).
3. **Open Map Stability**:
   - `02fields` verified 100% bit-for-bit identical to baseline (+0 net gems across both sides).

## 2. Build Instructions
Requirements: `cambc` CLI with WASI SDK 33.
```bash
cambc build V153/final_release_v1j_r6 --release
```
Target output: `.cambc/build-release/bot-injected.wasm`

## 3. Preservation
- `original_v153`: Protected and untouched.
- `champion_v2` (`V153/checkpoints/champion_v2`): Protected and untouched.
- `v1j_r6_checkpoint` (`V153/checkpoints/v1j_r6_checkpoint`): Protected and untouched.
- `candidate_v1m` (`V153/source/candidate_v1m`): Preserved for experiment archives.

