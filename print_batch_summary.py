import json

with open('evidence/v67_diagnostic/summary_25.json') as f:
    matches = json.load(f)

print('Total matches:', len(matches))
wins = sum(1 for m in matches if m['result'] == 'win')
losses = sum(1 for m in matches if m['result'] == 'loss')
print(f'OVERALL RECORD: {wins} W - {losses} L\n')

header = '{:<22} | {:<16} | {:<5} | {:<6} | {:<14} | {:<15} | {:<15}'.format(
    'Opponent', 'Map', 'Side', 'Result', 'Gems (Us/Them)', 'Kills (Us/Them)', 'Opponent Picks'
)
print(header)
print('-'*105)

by_opp = {}
for m in matches:
    opp = m['opponent']
    by_opp.setdefault(opp, []).append(m)
    g_str = str(m['our_gems']) + '/' + str(m['opp_gems'])
    k_str = str(m['our_kills']) + '/' + str(m['opp_kills'])
    row = '{:<22} | {:<16} | {:<5} | {:<6} | {:<14} | {:<15} | {:<15}'.format(
        opp, m['map'], m['our_side'].upper(), m['result'],
        g_str, k_str, str(m['opp_picks'])
    )
    print(row)

print('\n=== PER OPPONENT BREAKDOWN ===')
for opp, mlist in by_opp.items():
    o_wins = sum(1 for m in mlist if m['result'] == 'win')
    o_losses = sum(1 for m in mlist if m['result'] == 'loss')
    o_gems_us = sum(m['our_gems'] for m in mlist)
    o_gems_them = sum(m['opp_gems'] for m in mlist)
    o_k_us = sum(m['our_kills'] for m in mlist)
    o_k_them = sum(m['opp_kills'] for m in mlist)
    print('{:<22}: {}W - {}L | Gems: {} vs {} | Kills: {} vs {}'.format(
        opp, o_wins, o_losses, o_gems_us, o_gems_them, o_k_us, o_k_them
    ))

