import hashlib
import datetime

class Block:

	def __init__(self, previous_hash, data):
		self.previous_hash = previous_hash
		self.data = data
		self.timestamp = datetime.datetime.now()
		self.hash = self.compute_hash()
			
	def compute_hash(self):
		temp = hashlib.sha256()
		temp.update(str(self.previous_hash).encode('utf-8')+str(self.data).encode('utf-8')+str(self.timestamp).encode('utf-8'))
		return temp.hexdigest()
		
	@staticmethod
	def next(data, last_block):
		return Block(last_block.hash, data)
		
blocks = int(input("Enter no of blocks:"))

b = Block("0", "Genesis block Author: Vikram Kumar")

blockchain = []
blockchain.append(b)

for i in range(blocks):
	print("Enter data of block %d:"% i)
	data = input()
	
	previous = b
	
	b = Block.next(data, previous)
		
	blockchain.append(b)
	
	
block = 0
for blocks in blockchain:
	print("block :: %d {\n\tdata:\t\t%s\n\tprevious_hash:\t%s\n\tcurrent_hash:\t%s\n}\n"
	%(block,blocks.data, blocks.previous_hash, blocks.hash))
	block += 1