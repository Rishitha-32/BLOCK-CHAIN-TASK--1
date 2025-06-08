import hashlib
import time

class Block:
    def __init__(self, index, data, previousHash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        raw_data = str(self.index) + str(self.timestamp) + str(self.data) + self.previousHash + str(self.nonce)
        return hashlib.sha256(raw_data.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block with difficulty: {difficulty}...")
        target = '0' * difficulty
        start_time = time.time()
        attempts = 0

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()
        print(f"Block mined! Hash: {self.hash}")
        print(f"Nonce found after {attempts} attempts")
        print(f"⏱Time taken: {round(end_time - start_time, 4)} seconds")

# Create and mine a block
difficulty = 4  # You can change to 5 or more to see more attempts
block = Block(1, "Mining this block", "0")
block.mine_block(difficulty)
