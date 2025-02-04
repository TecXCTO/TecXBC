from flask import Flask, jsonify, request
from blockchain.chain import Blockchain
from blockchain.proof_of_work import ProofOfWork

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine_block():
    last_proof = blockchain.chain[-1].proof
    proof = ProofOfWork.proof_of_work(last_proof)
    blockchain.add_new_block(proof)
    return jsonify({'message': 'New block added'}), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message': 'Transaction added'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
