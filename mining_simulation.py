import hashlib
import time

class Block:
    def __init__(self, data):
        self.timestamp = time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        raw = str(self.timestamp) + self.data + str(self.nonce)
        return hashlib.sha256(raw.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        print(f"Mining block with difficulty {difficulty}...")
        start_time = time.time()

        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print(f"Block mined!\nHash: {self.hash}")
        print(f"Nonce used: {self.nonce}")
        print(f"Time taken: {round(end_time - start_time, 2)} seconds\n")

# Run the mining simulation
block = Block("This is a mined block by Ahmed")
block.mine_block(difficulty=4)
