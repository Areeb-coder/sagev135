import json
import glob

with open('match-a01310ef-1523-4fb1-bb68-0d3327b0660c.json') as f:
    d = json.load(f)

print('=== MATCH PERFORMANCE BREAKDOWN ===')
for t in d.get('teams', []):
    print(f"Team {t['team']}: Submitted Gems = {t['submittedGems']}")

stats = {'teamA': {'kills': 0, 'deaths': 0, 'gems_collected': 0, 'gems_lost': 0, 'camps': 0},
         'teamB': {'kills': 0, 'deaths': 0, 'gems_collected': 0, 'gems_lost': 0, 'camps': 0}}

for event_group in d.get('events', []):
    kind = event_group.get('kind')
    owner = event_group.get('owner', {})
    team = owner.get('team')
    entries = event_group.get('entries', [])
    count = len(entries)
    
    if team in stats:
        if kind == 'death':
            stats[team]['deaths'] += count
        elif kind == 'kill':
            stats[team]['kills'] += count
        elif kind == 'campClear':
            stats[team]['camps'] += count
        elif kind == 'gemCollection':
            stats[team]['gems_collected'] += sum(float(e.get('value', 0)) for e in entries)
        elif kind == 'gemLoss':
            stats[team]['gems_lost'] += sum(float(e.get('value', 0)) for e in entries)

print(json.dumps(stats, indent=2))

