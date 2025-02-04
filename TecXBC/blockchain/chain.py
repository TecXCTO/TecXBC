from .block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0", 1)
        self.chain.append(genesis_block)

    def add_new_block(self, proof):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), self.current_transactions, previous_block.hash_block(), proof)
        self.current_transactions = []
        self.chain.append(new_block)

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append(Transaction(sender, receiver, amount).to_dict())

    def is_valid_chain(self, chain):
        for i in range(1, len(chain)):
            if chain[i].previous_hash != chain[i-1].hash_block():
                return False
        return True
