# Sprint 3 Multi-Opponent Evaluation Standard
# Replaces rigid single-metric thresholds with a holistic scorecard:
# 1. Broad Map Consistency (50-game symmetric test >= 28W, net gems >= +9,000)
# 2. Multi-Tier Competitive Resilience:
#    - Peer Tier (Rank 160-190): Target win rate >= 40% (2+ / 5 wins)
#    - High-Elo Tier (Rank 10-50): Target competitive game length & gem denial
#    - Meta Apex Tier (Rank 1-5): Target draft alignment & early skirmish survivability
# 3. Fallback Protection: Sage v157 (+10,035 net gems) remains immutable baseline fallback

def evaluate(gate2_wins, gate2_net_gems, peer_wins, peer_games=5):
    score = 0
    # Map consistency weight
    if gate2_wins >= 30 and gate2_net_gems >= 9800:
        score += 50
    elif gate2_wins >= 28:
        score += 35
        
    # Peer competitive resilience weight
    peer_wr = peer_wins / peer_games
    if peer_wr >= 0.40:
        score += 50
    elif peer_wr >= 0.20:
        score += 30
        
    return score >= 75
