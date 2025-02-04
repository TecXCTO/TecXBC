import uuid

class Wallet:
    def __init__(self):
        self.address = str(uuid.uuid4()).replace('-', '')

    def get_address(self):
        return self.address
