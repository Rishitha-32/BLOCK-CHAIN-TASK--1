import random

# Validators with mock data
pow_validators = [
    {"name": "Miner A", "power": random.randint(50, 100)},
    {"name": "Miner B", "power": random.randint(50, 100)},
    {"name": "Miner C", "power": random.randint(50, 100)},
]

pos_validators = [
    {"name": "Staker A", "stake": random.randint(100, 1000)},
    {"name": "Staker B", "stake": random.randint(100, 1000)},
    {"name": "Staker C", "stake": random.randint(100, 1000)},
]

# Voters voting for delegates (DPoS)
dpos_delegates = {
    "Delegate A": 0,
    "Delegate B": 0,
    "Delegate C": 0,
}

voters = ["Voter1", "Voter2", "Voter3"]

# Each voter votes randomly for a delegate
for voter in voters:
    vote = random.choice(list(dpos_delegates.keys()))
    dpos_delegates[vote] += 1
    print(f"{voter} voted for {vote}")

print("\n--- Consensus Results ---\n")

# PoW: Select validator with highest power
pow_winner = max(pow_validators, key=lambda v: v["power"])
print(f"PoW Winner: {pow_winner['name']} with power {pow_winner['power']}")
print("Explanation: Miner with highest computational power is chosen.")

# PoS: Select validator with highest stake
pos_winner = max(pos_validators, key=lambda v: v["stake"])
print(f"PoS Winner: {pos_winner['name']} with stake {pos_winner['stake']}")
print("Explanation: Validator with highest stake is chosen.")

# DPoS: Select delegate with most votes
dpos_winner = max(dpos_delegates, key=dpos_delegates.get)
print(f"DPoS Winner: {dpos_winner} with votes {dpos_delegates[dpos_winner]}")
print("Explanation: Delegate with most votes is chosen by voters.")
