import hashlib

class ProofOfWork:
    @staticmethod
    def proof_of_work(last_proof):
        proof = 0
        while not ProofOfWork.is_valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def is_valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example: 4 leading zeroes
