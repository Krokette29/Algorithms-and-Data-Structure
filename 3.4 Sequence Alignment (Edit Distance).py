def sequenceAlignment(str1, str2, costs):
	subCost, gapCost = costs

	dp = [[None] * (len(str2) + 1) for _ in range(len(str1) + 1)]
	for i in range(len(dp)):
		dp[i][0] = i
	for j in range(len(dp[0])):
		dp[0][j] = j

	for i in range(1, len(dp)):
		for j in range(1, len(dp[0])):
			op1 = dp[i - 1][j - 1] + subCost if str1[i - 1] != str2[j - 1] else dp[i - 1][j - 1]
			op2 = dp[i - 1][j] + gapCost
			op3 = dp[i][j - 1] + gapCost
			dp[i][j] = min(op1, op2, op3)

	return dp


def reconstructions(str1, str2, costs, dp):
	subCost, gapCost = costs
	i, j = len(dp) - 1, len(dp[0]) - 1
	res1, res2 = '', ''

	while i > 0 and j > 0:
		if dp[i][j] == dp[i - 1][j] + gapCost:
			res1 = str1[i - 1] + res1
			res2 = '#' + res2
			i -= 1

		elif dp[i][j] == dp[i][j - 1] + gapCost:
			res1 = '#' + res1
			res2 = str2[j - 1] + res2
			j -= 1

		else:
			res1 = str1[i - 1] + res1
			res2 = str2[j - 1] + res2
			i -= 1
			j -= 1

	if i == 0:
		res1 = '#' * j + res1
		res2 = str2[:j] + res2
	elif j == 0:
		res1 = str1[:i] + res1
		res2 = '#' * i + res2

	return res1, res2


def main():
	str1 = "I have a dream"
	str2 = "I had a team"
	costs = [1, 1]		# substitution cost and gap cost

	dp = sequenceAlignment(str1, str2, costs)
	print("edit distance: ", dp[-1][-1])

	res1, res2 = reconstructions(str1, str2, costs, dp)
	print("string 1: ", res1)
	print("string 2: ", res2)


if __name__ == "__main__":
	main()
