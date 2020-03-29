from collections import deque
class Node(object):
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def optimalBST(freq):
	dp = [[None] * len(freq) for _ in range(len(freq))]

	for diff in range(len(freq)):
		for i in range(len(freq) - diff):
			j = i + diff
			sigmaFreq = sum(freq[i:j + 1])
			
			for root in range(i, j + 1):
				tmpCost = sigmaFreq
				if root != i: tmpCost += dp[i][root - 1]
				if root != j: tmpCost += dp[root + 1][j]
				dp[i][j] = min(dp[i][j], tmpCost) if dp[i][j] != None else tmpCost

	return dp


def reconstruction(keys, freq, dp, i=0, j=None):
	if j == None: j = len(freq) - 1
	if i > j: return None

	sigmaFreq = sum(freq[i:j + 1])
	for root in range(i, j + 1):
		tmpCost = sigmaFreq
		if root != i: tmpCost += dp[i][root - 1]
		if root != j: tmpCost += dp[root + 1][j]

		if dp[i][j] == tmpCost:
			rootNode = Node(keys[root])
			rootNode.left = reconstruction(keys, freq, dp, i, root - 1)
			rootNode.right = reconstruction(keys, freq, dp, root + 1, j)

	return rootNode


def main():
	keys = [i + 1 for i in range(7)]
	freq = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]

	dp = optimalBST(freq)
	print("Minimum total search time: ", dp[0][len(dp[0]) - 1])

	root = reconstruction(keys, freq, dp)
	print("root key: ", root.key)


if __name__ == "__main__":
	main()
