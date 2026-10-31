import subprocess, json, time, os

def check():
    with open('active_sprint3_matches.json') as f:
        data = json.load(f)
    
    all_done = True
    for g in data['groups']:
        gid = g['id']
        team = g['team']
        tier = g['tier']
        res = subprocess.run(['cambc', 'match-groups', 'show', gid, '--json'], capture_output=True, text=True)
        try:
            mdata = json.loads(res.stdout)
            matches = mdata.get('matches', [])
            statuses = [m.get('status') for m in matches]
            print(f'[{tier}] {team} ({gid}): {statuses}')
            if not all(s in ['completed', 'failed'] for s in statuses):
                all_done = False
        except Exception as e:
            print(f'Error reading {gid}: {e}')
            all_done = False
    return all_done

if __name__ == '__main__':
    check()
