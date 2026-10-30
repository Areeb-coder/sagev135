import json
import glob

files = glob.glob("evidence/diagnostics-v135/summary-*.json")

our_deaths_by_champ = {}
for f in files:
    with open(f) as fp:
        d = json.load(fp)
    for ev in d.get('events', []):
        if ev.get('kind') == 'death':
            owner = ev.get('owner', {})
            if owner.get('team') == 'teamA':
                name = owner.get('name')
                our_deaths_by_champ[name] = our_deaths_by_champ.get(name, 0) + len(ev.get('entries', []))

print("=== OUR DEATHS BY CHAMPION ===")
for c, cnt in sorted(our_deaths_by_champ.items(), key=lambda x: -x[1]):
    print(f"{c:<20}: {cnt} deaths")

