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
