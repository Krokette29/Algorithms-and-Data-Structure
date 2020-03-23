"""
3.Question 3
In this programming problem you'll code up Prim's minimum spanning tree algorithm.

This file (edges.txt) describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""

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
