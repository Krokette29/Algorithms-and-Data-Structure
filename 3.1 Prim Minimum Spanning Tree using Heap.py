import heapq
def heapDelete(arr, item):
	if arr[-1] == item: return arr[:-1]

	for index, value in enumerate(arr):
		if value == item:
			leaf = arr.pop()
			arr[index] = leaf

			if item[0] < leaf[0]:
				heapq._siftup(arr, index)
			else:
				heapq._siftdown(arr, 0, index)
			break
	else:
		raise ValueError("Delete Error!")

	return arr


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
	numVisitedNodes = 0

	# randomly choose starting node, here choose node 1
	visited[1] = True
	numVisitedNodes += 1

	# use heap to accelerate the algorithm
	heap = []			# stores (cost, node) for every unvisited node
	heapDict = {}		# stores (node, cost) for reverse searching
	for node, cost in nodes[1].connections:
		heapq.heappush(heap, (cost, node))
		heapDict[node] = cost

	while numVisitedNodes != len(nodes) - 1:
		try:
			# first value of heap is the minimum cost
			minCost, minNodeIndex = heapq.heappop(heap)

			visited[minNodeIndex] = True
			numVisitedNodes += 1
			totalCost += minCost
			del heapDict[minNodeIndex]

			# update the heap and heapDict after adding the minNode into MST
			for node, cost in nodes[minNodeIndex].connections:
				if not visited[node]:
					if node not in heapDict:
						heapq.heappush(heap, (cost, node))
						heapDict[node] = cost
					elif cost < heapDict[node]:
						heap = heapDelete(heap, (heapDict[node], node))
						heapq.heappush(heap, (cost, node))
						heapDict[node] = cost
		except IndexError:
			break

	if numVisitedNodes == len(nodes) - 1:
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
