import json
import glob
import os

files = glob.glob("evidence/diagnostics-v135/summary-*.json")
drafts = {}

for f in files:
    with open(f) as fp:
        d = json.load(fp)
    roster = d.get('roster', {}).get('draft', [])
    teamA_picks = [x['champion'] for x in roster if x['team'] == 'teamA']
    teamB_picks = [x['champion'] for x in roster if x['team'] == 'teamB']
    
    # identify opponent from teams
    for t in d.get('teams', []):
        if t['team'] == 'teamB':
            opp_gems = t['submittedGems']
    
    match_id = os.path.basename(f).replace('summary-', '').replace('.json', '')
    drafts[match_id] = {
        'teamA': teamA_picks,
        'teamB': teamB_picks
    }

print("=== OPPONENT DRAFT ANALYSIS ===")
opp_champ_counts = {}
for mid, d in drafts.items():
    for c in d['teamB']:
        opp_champ_counts[c] = opp_champ_counts.get(c, 0) + 1

for c, count in sorted(opp_champ_counts.items(), key=lambda x: -x[1]):
    print(f"{c:<20}: {count} picks")

print("\n=== OUR DRAFT ANALYSIS ===")
our_champ_counts = {}
for mid, d in drafts.items():
    for c in d['teamA']:
        our_champ_counts[c] = our_champ_counts.get(c, 0) + 1

for c, count in sorted(our_champ_counts.items(), key=lambda x: -x[1]):
    print(f"{c:<20}: {count} picks")

