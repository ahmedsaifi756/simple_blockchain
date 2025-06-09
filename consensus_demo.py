import random

# Mock Validators
miner = {'name': 'MinerX', 'power': random.randint(100, 1000)}
staker = {'name': 'StakerY', 'stake': random.randint(1000, 10000)}
voters = {
    'A': 'Validator1',
    'B': 'Validator2',
    'C': 'Validator1'  # Validator1 gets 2 votes
}

# PoW: Highest Power
print("\n PoW Consensus:")
print(f"Miner Power: {miner['power']}")
print(f"Selected: {miner['name']} (highest computational power)\n")

# PoS: Highest Stake
print("PoS Consensus:")
print(f"Staker Stake: {staker['stake']}")
print(f"Selected: {staker['name']} (highest coin stake)\n")

# DPoS: Most Voted Validator
vote_counts = {}
for v in voters.values():
    vote_counts[v] = vote_counts.get(v, 0) + 1
delegate = max(vote_counts, key=vote_counts.get)

print("DPoS Consensus:")
print("Votes:", voters)
print(f"Selected: {delegate} (elected by votes)\n")
