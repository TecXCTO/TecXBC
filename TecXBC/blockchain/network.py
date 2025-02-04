import requests

class NodeNetwork:
    def __init__(self):
        self.nodes = set()

    def add_node(self, address):
        self.nodes.add(address)

    def sync_chain(self):
        longest_chain = None
        max_length = len(self.chain)

        for node in self.nodes:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length:
                    max_length = length
                    longest_chain = chain

        if longest_chain:
            self.chain = longest_chain
            return True
        return False
