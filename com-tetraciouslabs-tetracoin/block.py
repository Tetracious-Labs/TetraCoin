# A block is a unique record in the blockchain
# we'll keep all data relating to the block within the block class

import datetime as d
import hashlib as h
import json

class Block(object):
    def __init__(self, index, timestamp, transactions, lastHash, lastBlock):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.hash
        self.lastHash = lastHash
        self.lastBlock = lastBlock

    def hash(self):
        blockEncryption = h.sha256()
        blockEncryption.update(str(self.index) + str(self.timestamp) + str(self.transactions) + self.lastHash)
        return blockEncryption.hexdigest()

    # store block data in json format
    def JsonEncode(self):
        return json.dumps(self.__dict__, sort_keys=True, default=str)

    @staticmethod
    def GenesisBlock():
        return Block.JsonEncode(Block(0, d.datetime.now(), "Genesis Transaction", None, None))

    @staticmethod
    def createNewBlock():
        return