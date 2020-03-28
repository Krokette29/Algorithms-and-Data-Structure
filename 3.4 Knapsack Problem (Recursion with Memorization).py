"""
2.Question 2
This problem also asks you to solve a knapsack instance, but a much bigger one.

This file (knapsack_big.txt) describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

import sys
sys.setrecursionlimit(10**6)		# set larger limit of recursion

def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	size, numItems = list(map(int, data[0].split()))
	values, weights = [], []
	for i in range(1, len(data)):
		v, w = list(map(int, data[i].split()))
		values.append(v)
		weights.append(w)
	return size, numItems, values, weights


def knapsackMemorization(size, numItems, values, weights):
	# use recursion with memorization to calculate the "needed" values instead of every single value
	def helper(size, numItems):
		if size < 0: return None
		if (numItems, size) in dp.keys():
			return dp[(numItems, size)]

		op1 = helper(size - weights[numItems - 1], numItems - 1)
		op2 = helper(size, numItems - 1)
		dp[(numItems, size)] = max(op1 + values[numItems - 1], op2) if op1 != None else op2
		return dp[(numItems, size)]

	# use dict instead of list to make better usage of memory
	dp = {}
	for i in range(size + 1):
		dp[(0, i)] = 0

	return helper(size, numItems)


def main():
	filePath = "data/knapsack_big.txt"
	size, numItems, values, weights = dataReader(filePath)
	ans = knapsackMemorization(size, numItems, values, weights)
	print(ans)


if __name__ == "__main__":
	main()
