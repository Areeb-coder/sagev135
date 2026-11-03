"""
Evaluation script for EXP-0176-A (Ryth Frontline small-team draft vs Baseline v175).
Reads 10 side-swapped match statistics from experiments/EXP-0176-A/
"""
import json
from pathlib import Path

BASE = Path("E:/Projects/Bot/LockIN")
EXP_DIR = BASE / "experiments/EXP-0176-A"

MAPS = [
    ("00anvil", 1, 2),
    ("00packs", 3, 4),
    ("02arena", 5, 6),
    ("00oasis", 7, 8),
    ("01hooks", 9, 10),
]

def eval_experiment():
    cand_wins = 0
    base_wins = 0
    cand_gems = 0
    base_gems = 0
    
    print("=====================================================================")
    print("EXP-0176-A EVALUATION: Candidate (Ryth Frontline) vs Baseline (v175)")
    print("=====================================================================")
    
    for map_name, id_a, id_b in MAPS:
        stat_a_path = EXP_DIR / f"m{id_a:02d}_{map_name}_canda.json"
        stat_b_path = EXP_DIR / f"m{id_b:02d}_{map_name}_candb.json"
        
        if not stat_a_path.exists() or not stat_b_path.exists():
            print(f"[-] {map_name}: Stats files not found yet.")
            continue
            
        da = json.loads(stat_a_path.read_text(encoding="utf-8"))
        db = json.loads(stat_b_path.read_text(encoding="utf-8"))
        
        # Match A: Team A is Candidate, Team B is Baseline
        # outcome is 'teamA' or 'teamB'
        win_a = da['match']['outcome'] == 'teamA'
        gems_cand_a = int(da['teams'][0]['submittedGems'])
        gems_base_a = int(da['teams'][1]['submittedGems'])
        
        # Match B: Team A is Baseline, Team B is Candidate
        win_b = db['match']['outcome'] == 'teamB'
        gems_base_b = int(db['teams'][0]['submittedGems'])
        gems_cand_b = int(db['teams'][1]['submittedGems'])
        
        m_cand_wins = (1 if win_a else 0) + (1 if win_b else 0)
        cand_wins += m_cand_wins
        base_wins += (2 - m_cand_wins)
        
        tot_cand_gems = gems_cand_a + gems_cand_b
        tot_base_gems = gems_base_a + gems_base_b
        cand_gems += tot_cand_gems
        base_gems += tot_base_gems
        
        delta = tot_cand_gems - tot_base_gems
        print(f"[{'WIN' if m_cand_wins >= 2 else ('DRAW' if m_cand_wins == 1 else 'LOSS')}] {map_name:15} | Score: {m_cand_wins}-{(2-m_cand_wins)} | Cand Gems: {tot_cand_gems} vs Base: {tot_base_gems} (Delta: {delta:+d})")

    print("---------------------------------------------------------------------")
    print(f"TOTAL: Candidate {cand_wins}W - {base_wins}L Baseline")
    print(f"NET GEMS: Candidate {cand_gems} vs Baseline {base_gems} (Delta: {cand_gems - base_gems:+d})")
    print("=====================================================================")

if __name__ == "__main__":
    eval_experiment()

