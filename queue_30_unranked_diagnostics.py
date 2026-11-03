# Auto-generated 30-match unranked diagnostic runner
# Target: 6 strong opponents x 5 matches = 30 matches (balanced sides: a,b,a,b,a)
# Opponents:
# 1. cache_v2                   (b593565f-9ebc-49e2-807b-e29d72fbd365)
# 2. Mite                       (ee83f5e5-bcad-4923-86b4-b79ea6083d2e)
# 3. Intercontinental Fish      (1890540d-1ffc-4847-adbf-d0d08772f268)
# 4. Univardisty of Shingtonwash (a4350547-b7a1-47b1-9031-4f7f084ad0d8)
# 5. NEETCoders                 (882106d4-9deb-40cc-9d5c-8522c1d32129)
# 6. Claude wrote everything     (ad62d13f-0ea0-4d3d-9773-3d7bf50813e4)

MAPS = '00expanse,02fields,00lanes,00anvil,01hooks'
SIDES = 'a,b,a,b,a'

OPPONENTS = [
    ('b593565f-9ebc-49e2-807b-e29d72fbd365', 'cache_v2'),
    ('ee83f5e5-bcad-4923-86b4-b79ea6083d2e', 'Mite'),
    ('1890540d-1ffc-4847-adbf-d0d08772f268', 'Intercontinental Fish'),
    ('a4350547-b7a1-47b1-9031-4f7f084ad0d8', 'Univardisty of Shingtonwash'),
    ('882106d4-9deb-40cc-9d5c-8522c1d32129', 'NEETCoders'),
    ('ad62d13f-0ea0-4d3d-9773-3d7bf50813e4', 'Claude wrote everything'),
]

import subprocess, json, time

def queue_diagnostics():
    created_groups = []
    print('Starting 30-match diagnostic queuing (6 match groups of 5)...')
    for opp_id, name in OPPONENTS:
        cmd = [
            'cambc', 'match-groups', 'create', opp_id,
            '--maps', MAPS,
            '--sides', SIDES,
            '--json'
        ]
        print(f'Queueing vs {name} ({opp_id})...')
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            try:
                data = json.loads(res.stdout)
                gid = data.get('id', data.get('groupId', res.stdout.strip()))
                print(f'  [+] Success: Group ID {gid}')
                created_groups.append({'opponent': name, 'id': gid})
            except:
                print(f'  [+] Output: {res.stdout.strip()}')
        else:
            print(f'  [-] Failed: {res.stderr.strip()}')
        time.sleep(1)

    with open('diagnostic_30_created_groups.json', 'w') as f:
        json.dump(created_groups, f, indent=2)
    print(f'Finished queuing. Saved to diagnostic_30_created_groups.json')

if __name__ == '__main__':
    queue_diagnostics()
