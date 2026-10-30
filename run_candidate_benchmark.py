import subprocess
import json
import os

maps = [
    "00vault",
    "00collision",
    "00contest",
    "00corners",
    "01starfish",
    "02fields",
    "00great-wall",
    "01shortcut",
    "01boss-battle",
    "01the-farm",
    "02the-pond",
    "00dunes"
]

results = []
wins_cand = 0
wins_base = 0
total_kills_cand = 0
total_kills_base = 0
total_gems_cand = 0
total_gems_base = 0

for m in maps:
    for swap in [False, True]:
        bot_a = "bots/v67_baseline" if swap else "bots/candidate_v67"
        bot_b = "bots/candidate_v67" if swap else "bots/v67_baseline"
        label_cand = "B" if swap else "A"
        label_base = "A" if swap else "B"
        
        stat_file = f"scrim_v67_{m}_swap{int(swap)}.json"
        cmd = [
            "cambc.exe", "run", bot_a, bot_b,
            "--release", "--map", m,
            "--statistics", stat_file, "--json"
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        winner_line = "Unknown"
        for line in proc.stdout.splitlines():
            if "wins:" in line:
                winner_line = line.strip()
        
        gems_cand = 0
        gems_base = 0
        kills_cand = 0
        kills_base = 0
        winner = "candidate_v67" if "candidate_v67" in winner_line else ("v67_baseline" if "v67_baseline" in winner_line else "Unknown")
        
        if os.path.exists(stat_file):
            try:
                with open(stat_file) as f:
                    data = json.load(f)
                    for t in data.get("teams", []):
                        tm = t.get("team")
                        sub = int(t.get("submittedGems", 0))
                        if (tm == "teamA" and not swap) or (tm == "teamB" and swap):
                            gems_cand = sub
                        else:
                            gems_base = sub
                    for c in data.get("championTimelines", []):
                        if c.get("metric") == "kills":
                            tm = c.get("owner", {}).get("team")
                            pts = c.get("points", [])
                            val = int(pts[-1].get("value", 0)) if pts else 0
                            if (tm == "teamA" and not swap) or (tm == "teamB" and swap):
                                kills_cand += val
                            else:
                                kills_base += val
            except Exception as e:
                pass
            try:
                os.remove(stat_file)
            except:
                pass
                
        if winner == "candidate_v67":
            wins_cand += 1
        elif winner == "v67_baseline":
            wins_base += 1
            
        total_kills_cand += kills_cand
        total_kills_base += kills_base
        total_gems_cand += gems_cand
        total_gems_base += gems_base
        
        side_cand = "Side B" if swap else "Side A"
        side_base = "Side A" if swap else "Side B"
        print(f"[{m:<14}] {side_cand} (cand) vs {side_base} (base) -> Winner: {winner:<13} | Gems: {gems_cand:>4} vs {gems_base:>4} | Kills: {kills_cand:>2} vs {kills_base:>2}")

print("\n" + "="*24 + " 24-GAME SYMMETRIC BENCHMARK REPORT " + "="*24)
print(f"Match Score : candidate_v67: {wins_cand} wins | v67_baseline: {wins_base} wins")
print(f"Total Gems  : candidate_v67: {total_gems_cand} | v67_baseline: {total_gems_base}")
print(f"Total Kills : candidate_v67: {total_kills_cand} | v67_baseline: {total_kills_base}")
print("="*80)

