import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block #{self.index}:\nData: {self.data}\nHash: {self.hash}\nPrevious Hash: {self.previous_hash}\n"

# Creating the blockchain
print("Creating 3 block chain...\n")

block1 = Block(1, time.time(), "Ahmed sends 5 BTC to Ali", "0")
block2 = Block(2, time.time(), "Ali sends 2 BTC to Sara", block1.hash)
block3 = Block(3, time.time(), "Sara sends 1 BTC to Zaid", block2.hash)

# Displaying the chain
print(block1)
print(block2)
print(block3)

# Tampering Block 1
print("\n Now changing data in Block 1 and recalculating its hash...\n")
block1.data = "Ahmed sends 50 BTC to Ali"
block1.hash = block1.calculate_hash()

# Re-checking hashes
print(block1)
print(block2)
print(block3)

print("Notice: Block 2's `previous_hash` doesn't match tampered Block 1's new hash!\n Chain broken.\n")
