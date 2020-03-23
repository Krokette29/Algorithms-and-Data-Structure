"""
2.Question 2
In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The format (clustering_big.txt) is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes uu and vv in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of kk such that there is a kk-clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?
"""

class UFS(object):
	def __init__(self, length):
		self.p = [i for i in range(length)]
		self.rank = [0 for _ in range(length)]

	def find(self, x):
		if self.p[x] != x:
			self.p[x] = self.find(self.p[x])
		return self.p[x]

	def union(self, x, y):
		rx, ry = self.find(x), self.find(y)
		if self.rank[rx] < self.rank[ry]:
			self.p[rx] = ry
		elif self.rank[rx] > self.rank[ry]:
			self.p[ry] = rx
		else:
			self.p[rx] = ry
			self.rank[ry] += 1


def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	numNodes, numBits = list(map(int, data[0].split()))
	nodeValueToID = {}
	for i in range(1, len(data)):
		value = data[i].replace(' ', '')
		value = int(value, 2)

		if value not in nodeValueToID:
			nodeValueToID[value] = [i - 1]
		else:
			nodeValueToID[value].append(i - 1)

	return numNodes, numBits, nodeValueToID


def countCluster(numNodes, numBits, nodeValueToID):
	ufs = UFS(numNodes)

	# 0 Hamming distance
	for nodeValue, nodeIDList in nodeValueToID.items():
		if len(nodeIDList) > 1:
			for i in range(1, len(nodeIDList)):
				numNodes -= 1
				ufs.union(nodeIDList[0], nodeIDList[i])

	# 1 Hamming distance
	for nodeValue, nodeIDList in nodeValueToID.items():
		for i in range(numBits):
			mask = 1 << i
			newNodeValue = nodeValue ^ mask

			if newNodeValue in nodeValueToID:
				newNodeID = nodeValueToID[newNodeValue][0]
				if ufs.find(nodeIDList[0]) != ufs.find(newNodeID):
					numNodes -= 1
					ufs.union(nodeIDList[0], newNodeID)
	
	# 2 Hamming distance
	for nodeValue, nodeIDList in nodeValueToID.items():
		for i in range(numBits - 1):
			for j in range(i + 1, numBits):
				mask = (1 << i) ^ (1 << j)
				newNodeValue = nodeValue ^ mask

				if newNodeValue in nodeValueToID:
					newNodeID = nodeValueToID[newNodeValue][0]
					if ufs.find(nodeIDList[0]) != ufs.find(newNodeID):
						numNodes -= 1
						ufs.union(nodeIDList[0], newNodeID)

	return numNodes


def main():
	filePath = "data/clustering_big.txt"
	numNodes, numBits, nodesCounter = dataReader(filePath)

	numClusters = countCluster(numNodes, numBits, nodesCounter)
	print("Largest value of k: ", numClusters)


if __name__ == "__main__":
	main()
