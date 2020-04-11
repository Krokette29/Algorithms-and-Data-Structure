"""
1.Question 1
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files describing three graphs:

g1.txt
g2.txt
g3.txt
The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute minu,v∈Vd(u,v), where d(u,v)d(u,v) denotes the shortest-path distance from uu to vv).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

OPTIONAL: Here is a bigger data set to play with.

large.txt
For fun, try computing the shortest shortest path of the graph in the file above.
"""

def dataReader(filePath):
	print("Start reading data...")

	with open(filePath) as f:
		data = f.readlines()

	numNodes, numEdges = list(map(int, data[0].split()))
	edgeCosts = {}
	for i in range(1, len(data)):
		li = list(map(int, data[i].split()))
		edge = tuple(li[:2])
		edgeCosts[edge] = li[2] if edge not in edgeCosts else min(li[2], edgeCosts[edge])

	print("Reading data complete.")
	return numNodes, numEdges, edgeCosts


def FloydWarshall(numNodes, numEdges, edgeCosts):
	print("Start FloydWarshall Algorithm...")

	# initialize dp matrix
	dp = [[None] * numNodes for _ in range(numNodes)]
	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if i == j:
				if (i + 1, j + 1) in edgeCosts and edgeCosts[(i + 1, j + 1)] < 0: return None
				dp[i][j] = 0
			elif (i + 1, j + 1) in edgeCosts:
				dp[i][j] = edgeCosts[(i + 1, j + 1)]
			else:
				continue

	# algorithm
	for k in range(numNodes):
		if k % 100 == 0: print("k = ", k)
		dpPrev = dp
		dp = [[None] * numNodes for _ in range(numNodes)]

		for i in range(len(dp)):
			for j in range(len(dp[0])):
				case1 = dpPrev[i][j]
				if dpPrev[i][k] == None: case2 = dpPrev[i][k]
				elif dpPrev[k][j] == None: case2 = dpPrev[k][j]
				else: case2 = dpPrev[i][k] + dpPrev[k][j]

				if case1 != None and case2 != None: dp[i][j] = min(case1, case2)
				elif case1 == None: dp[i][j] = case2
				else: dp[i][j] = case1

	# find the minimum
	minPathCost = None
	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if i == j and dp[i][i] < 0:
				print("There is a negative-cost cycle!")
				return None

			if i != j and dp[i][j] != None:
				minPathCost = min(minPathCost, dp[i][j]) if minPathCost != None else dp[i][j]

	print("Find the minimum path cost: ", minPathCost)
	return minPathCost


def main():
	filePaths = ["data/g1.txt", "data/g2.txt", "data/g3.txt"]

	ans = []
	for filePath in filePaths:
		print("======>> filePath = ", filePath)
		numNodes, numEdges, edgeCosts = dataReader(filePath)
		minPathCost = FloydWarshall(numNodes, numEdges, edgeCosts)
		ans.append(minPathCost)

	print("Final results of three graphs: ", ans)


if __name__ == "__main__":
	main()
