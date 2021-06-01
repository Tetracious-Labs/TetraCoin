# our blockchain class will act as a table
from block import Block
import datetime as d
import json
import pprint as pp

class BlockChain(object):
    def __init__(self):
        self.chain = [Block.GenesisBlock()]

    # Function to add blocks to the chain
    def AddBlock(self):
        index = len(self.chain)
        lastBlock = len(self.chain) - 1
        dict = json.loads(self.chain[lastBlock])
        self.chain.append(Block.JsonEncode(Block(index, d.datetime.now(), "transaction " + str(index + 1), dict['hash'], dict['index'])))