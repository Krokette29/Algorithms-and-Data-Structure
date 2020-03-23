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
