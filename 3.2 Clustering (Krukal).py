"""
1.Question 1
In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering.

This file (clustering1.txt) describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j)(i,j) for each choice of 1≤i<j≤n, where nn is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number kk of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

class Node(object):
	def __init__(self, value):
		self.nodeID = value
		self.connections = []


class Edge(object):
	def __init__(self, node1ID, node2ID, cost):
		self.nodes = (node1ID, node2ID)
		self.cost = cost


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

	numNodes = int(data[0])
	nodes = [Node(i) for i in range(numNodes + 1)]
	edges = []
	for index in range(1, len(data)):
		node1ID, node2ID, cost = list(map(int, data[index].split()))

		nodes[node1ID].connections.append((node2ID, cost))
		nodes[node2ID].connections.append((node1ID, cost))

		edges.append(Edge(node1ID, node2ID, cost))

	return numNodes, nodes, edges


def clustering(numClusters, numNodes, nodes, edges):
	ufs = UFS(numNodes + 1)
	findRes = False

	edges.sort(key=lambda item:item.cost)
	for edge in edges:
		node1ID, node2ID = edge.nodes
		if ufs.find(node1ID) != ufs.find(node2ID):
			if not findRes:
				ufs.union(node1ID, node2ID)
				numNodes -= 1
			else:
				return edge.cost

		if numNodes == numClusters:
			findRes = True


def main():
	filePath = "data/clustering1.txt"
	numNodes, nodes, edges = dataReader(filePath)
	minimumSpacing = clustering(4, numNodes, nodes, edges)
	print("Minimum Spacing of 4 clusters: ", minimumSpacing)


if __name__ == "__main__":
	main()
