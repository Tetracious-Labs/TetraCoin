from tetracoin.blockchain import BlockChain
import pprint as pp

def test_blockchain_initalise():
    blockchain = BlockChain()
    pp.pprint(blockchain.chain)
