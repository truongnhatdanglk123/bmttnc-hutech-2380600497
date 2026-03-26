from blockchain import Blockchain

# tạo blockchain
my_blockchain = Blockchain()

# thêm giao dịch
my_blockchain.add_transaction("Alice", "Bob", 10)
my_blockchain.add_transaction("Bob", "Charlie", 5)
my_blockchain.add_transaction("Charlie", "Alice", 3)

# đào block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof

proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

my_blockchain.add_transaction("Genesis", "Miner", 1)

block = my_blockchain.create_block(proof, previous_hash)

# hiển thị blockchain
for block in my_blockchain.chain:
    print("\n-------------------------")
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)

# kiểm tra hợp lệ
print("\nBlockchain valid:", my_blockchain.is_chain_valid(my_blockchain.chain))