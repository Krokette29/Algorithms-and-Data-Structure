"""
1.Question 1
In this programming problem and the next you'll code up the knapsack algorithm from lecture.

Let's start with a warm-up.

This file (knapsack1.txt) describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

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


def knapsackDP(size, numItems, values, weights):
	dp = [[None] * (size + 1) for _ in range(numItems + 1)]
	for i in range(len(dp[0])):
		dp[0][i] = 0

	for i in range(1, len(dp)):
		for j in range(len(dp[0])):
			w = weights[i - 1]
			if j >= w:
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + values[i - 1])
			else:
				dp[i][j] = dp[i - 1][j]

	return dp[-1][-1]


def main():
	filePath = "data/knapsack1.txt"
	size, numItems, values, weights = dataReader(filePath)
	ans = knapsackDP(size, numItems, values, weights)
	print(ans)


if __name__ == "__main__":
	main()
	