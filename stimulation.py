import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previousHash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        raw_data = str(self.index) + str(self.timestamp) + str(self.data) + self.previousHash + str(self.nonce)
        return hashlib.sha256(raw_data.encode()).hexdigest()

# Create 3 linked blocks
blockchain = []
genesis_block = Block(0, time.time(), "Genesis Block", "0")
blockchain.append(genesis_block)

second_block = Block(1, time.time(), "Second Block", blockchain[-1].hash)
blockchain.append(second_block)

third_block = Block(2, time.time(), "Third Block", blockchain[-1].hash)
blockchain.append(third_block)

# Print each block
for block in blockchain:
    print(f"Block {block.index} - Hash: {block.hash}, PrevHash: {block.previousHash}")

# Tamper Block 1
print("\n🔧 Tampering Block 1 data...\n")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Print blocks again
for block in blockchain:
    print(f"Block {block.index} - Hash: {block.hash}, PrevHash: {block.previousHash}")
