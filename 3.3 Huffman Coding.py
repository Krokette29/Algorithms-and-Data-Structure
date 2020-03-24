"""
1.Question 1
In this programming problem and the next you'll code up the greedy algorithm from the lectures on Huffman coding.

This file (huffman.txt) describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. What is the maximum length of a codeword in the resulting Huffman code?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

2.Question 2
Continuing the previous problem, what is the minimum length of a codeword in your Huffman code?
"""

import heapq
class Node(object):
	def __init__(self, ID, weight):
		self.ID = ID
		self.weight = weight
		self.left = None
		self.right = None
		self.minHeight = 0
		self.maxHeight = 0


def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	numSymbols = int(data[0])
	weights = []
	IDtoNode = {}
	for i in range(1, len(data)):
		weight = int(data[i])
		weights.append((weight, i))
		IDtoNode[i] = Node(i, weight)

	return numSymbols, weights, IDtoNode


def HuffmanCoding(numSymbols, weights, IDtoNode):
	'''
	Can also be implemented by sorting + two-queues.
	'''
	ID = numSymbols + 1

	heapq.heapify(weights)
	while len(weights) > 1:
		# pick two least weighted symbols, and calculate the new weight
		pop1, pop2 = heapq.heappop(weights), heapq.heappop(weights)
		newWeight = pop1[0] + pop2[0]
		heapq.heappush(weights, (newWeight, ID))

		# construct merged node
		newNode = Node(ID, newWeight)
		newNode.left = IDtoNode[pop1[1]]
		newNode.right = IDtoNode[pop2[1]]
		newNode.minHeight = min(newNode.left.minHeight, newNode.right.minHeight) + 1
		newNode.maxHeight = max(newNode.left.maxHeight, newNode.right.maxHeight) + 1
		IDtoNode[ID] = newNode

		ID += 1

	root = IDtoNode[ID - 1]
	return root


def main():
	filePath = "data/huffman.txt"
	numSymbols, weights, IDtoNode = dataReader(filePath)
	root = HuffmanCoding(numSymbols, weights, IDtoNode)
	print(root.minHeight, root.maxHeight)


if __name__ == "__main__":
	main()
