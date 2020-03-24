"""
3.Question 3
In this programming problem you'll code up the dynamic programming algorithm for computing a maximum-weight independent set of a path graph.

This file (mwis.txt) describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from lecture on this data set. The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set? (By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.) In the box below, enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and the other four vertices are not, then you should enter the string 10011010 in the box below.
"""

def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	numVertices = int(data[0])
	weights = list(map(int, data[1:]))
	return numVertices, weights


def DynamicProgramming(numVertices, weights):
	dp = [None] * (numVertices + 1)
	dp[0], dp[1] = 0, weights[0]

	for i in range(2, len(dp)):
		dp[i] = max(dp[i - 1], dp[i - 2] + weights[i - 1])

	return dp


def reconstruction(dp):
	path = [False] * len(dp)
	i = len(dp) - 1
	while i > 0:
		if dp[i] == dp[i - 1]:
			i -= 1
		else:
			path[i] = True
			i -= 2
	return path


def main():
	filePath = "data/mwis.txt"
	numVertices, weights = dataReader(filePath)
	dp = DynamicProgramming(numVertices, weights)
	path = reconstruction(dp)
	vertices = [1, 2, 3, 4, 17, 117, 517, 997]
	for v in vertices:
		print("Vertex {} contained: {}".format(v, path[v]))


if __name__ == "__main__":
	main()
