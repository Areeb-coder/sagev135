import json
import glob
import os
import subprocess

match_ids = [
    # Mite
    "a01310ef-1523-4fb1-bb68-0d3327b0660c",
    "234eeae6-fa3b-4c07-8c2a-753fe8210579",
    "dd2d45ca-52fd-42ee-ae19-b4526a60e3bc",
    "9991312e-1d2b-4128-a5d7-54f2a49fff2e",
    "d91bad4e-db76-4f49-b5a2-3bf32b354ca4",
    # Ad Astra
    "29c28ab6-d4c8-476a-af10-7b31f9e1f613",
    "b1ede09f-9bfe-44dd-9383-f586ebcd1f5d",
    "5f9325cc-b834-4aaf-9aff-5cb37541a93d",
    "e165b313-ccf3-4586-9a53-51dd3026e145",
    "c9f60f53-7653-4678-b58e-e3257baf990c",
    # NEETCoders
    "e4437cd7-5274-4651-a855-9e360224207d",
    "423004cc-97bd-49c9-8933-3f2461c97cac",
    "871b7a3b-3d72-4bdd-8ef4-c249bceebeff",
    "734dbb56-94b1-48e8-9c3c-2e2a133bb298",
    "67932c7c-67c5-4b57-9b57-b0781e091bef"
]

all_stats = []

for mid in match_ids:
    fname = f"evidence/diagnostics-v135/summary-{mid}.json"
    if not os.path.exists(fname):
        subprocess.run(["cambc", "matches", "summary", mid, "-o", fname, "--json"], stdout=subprocess.DEVNULL)
    
    if os.path.exists(fname):
        with open(fname) as f:
            d = json.load(f)
        
        teams = {t['team']: t['submittedGems'] for t in d.get('teams', [])}
        
        s = {'mid': mid,
             'map': d.get('match', {}).get('mapHash', 'unknown'),
             'rounds': d.get('match', {}).get('roundsCompleted', 0),
             'a_gems': teams.get('teamA', 0),
             'b_gems': teams.get('teamB', 0),
             'a_deaths': 0, 'b_deaths': 0,
             'a_kills': 0, 'b_kills': 0,
             'a_camps': 0, 'b_camps': 0}
        
        for ev in d.get('events', []):
            kind = ev.get('kind')
            team = ev.get('owner', {}).get('team')
            cnt = len(ev.get('entries', []))
            if team == 'teamA':
                if kind == 'death': s['a_deaths'] += cnt
                elif kind == 'kill': s['a_kills'] += cnt
                elif kind == 'campClear': s['a_camps'] += cnt
            elif team == 'teamB':
                if kind == 'death': s['b_deaths'] += cnt
                elif kind == 'kill': s['b_kills'] += cnt
                elif kind == 'campClear': s['b_camps'] += cnt
        
        all_stats.append(s)

print(f"{'Match ID':<10} | {'Rounds':<6} | {'Our Gems':<8} | {'Opp Gems':<8} | {'Our K/D':<8} | {'Opp K/D':<8} | {'Camps (Ours/Opp)':<15}")
print("-" * 80)
total_a_gems = 0
total_b_gems = 0
total_a_deaths = 0
total_b_deaths = 0

for s in all_stats:
    total_a_gems += int(s['a_gems'])
    total_b_gems += int(s['b_gems'])
    total_a_deaths += s['a_deaths']
    total_b_deaths += s['b_deaths']
    print(f"{s['mid'][:8]:<10} | {s['rounds']:<6} | {s['a_gems']:<8} | {s['b_gems']:<8} | {s['a_kills']}/{s['a_deaths']:<6} | {s['b_kills']}/{s['b_deaths']:<6} | {s['a_camps']}/{s['b_camps']:<15}")

print("-" * 80)
print(f"TOTALS: Our Gems: {total_a_gems} vs Opp Gems: {total_b_gems} | Our Deaths: {total_a_deaths} vs Opp Deaths: {total_b_deaths}")

