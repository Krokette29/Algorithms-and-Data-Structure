class Node(object):
	def __init__(self, index):
		self.index = index
		self.connections = []


def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	for index, item in enumerate(data):
		if index == 0:
			numNodes, numEdges = list(map(int, item.split()))
			nodes = [Node(index) for index in range(numNodes + 1)]

		else:
			node1, node2, cost = list(map(int, item.split()))
			nodes[node1].connections.append((node2, cost))
			nodes[node2].connections.append((node1, cost))

	return numNodes, numEdges, nodes


def PRIM_minimumSpanningTree(nodes):
	totalCost = 0
	visited = [False] * len(nodes)
	visitedNodes = []

	# randomly choose starting node, here choose node 1
	visited[1] = True
	visitedNodes.append(nodes[1])

	while len(visitedNodes) != len(nodes) - 1:
		minCost = None
		minNode = None

		# using Brute Force to search the minimum cost
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
	numNodes, numEdges, nodes = dataReader(filePath)
	totalCost = PRIM_minimumSpanningTree(nodes)
	print("Total cost of MST: ", totalCost)


if __name__ == "__main__":
	main()
