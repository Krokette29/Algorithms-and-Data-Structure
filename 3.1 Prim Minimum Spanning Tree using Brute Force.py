class Node(object):
	def __init__(self, index):
		self.index = index
		self.connections = []


class Edge(object):
	def __init__(self, node1, node2, cost):
		self.nodes = [node1, node2]
		self.cost = cost


def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	edges = []
	for index, item in enumerate(data):
		if index == 0:
			numNodes, numEdges = list(map(int, item.split()))
			nodes = [Node(index) for index in range(numNodes + 1)]

		else:
			item = list(map(int, item.split()))
			edges.append(Edge(item[0], item[1], item[2]))
			nodes[item[0]].connections.append((item[1], item[2]))
			nodes[item[1]].connections.append((item[0], item[2]))

	return numNodes, numEdges, edges, nodes


def PRIM_minimumSpanningTree(nodes):
	totalCost = 0
	visited = [False] * len(nodes)
	visitedNodes = []

	visited[1] = True
	visitedNodes.append(nodes[1])
	while len(visitedNodes) != len(nodes) - 1:
		minCost = None
		minNode = None
		for node in visitedNodes:
			for otherNodeIndex, otherCost in node.connections:
				if not visited[otherNodeIndex] and (minCost == None or otherCost < minCost):
					minCost = otherCost
					minNode = nodes[otherNodeIndex]

		if minNode:
			visited[minNode.index] = True
			visitedNodes.append(minNode)
			totalCost += minCost
		else:
			break

	if len(visitedNodes) == len(nodes) - 1:
		print("The graph is connected.")
	else:
		print("The graph is not connected.")

	return totalCost


def main():
	filePath = "data/edges.txt"
	numNodes, numEdges, edges, nodes = dataReader(filePath)
	totalCost = PRIM_minimumSpanningTree(nodes)
	print("Total cost of MST: ", totalCost)


if __name__ == "__main__":
	main()
