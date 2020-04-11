"""
1.Question 1
In this assignment you will implement one or more algorithms for the 2SAT problem. Here are 6 different 2SAT instances:

2sat1.txt
2sat2.txt
2sat3.txt
2sat4.txt
2sat5.txt
2sat6.txt
The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not". For example, the second line of the first data file is "-16808 75250", which indicates the clause ¬x16808∨x75250.

Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise. For example, if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string 111000 in the box below.

DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want. For example, 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per variable and two directed edges per clause, you should think through the details). This might be an especially attractive option for those of you who coded up an SCC algorithm in Part 2 of this specialization. Alternatively, you can use Papadimitriou's randomized local search algorithm. (The algorithm from lecture is probably too slow as stated, so you might want to make one or more simple modifications to it --- even if this means breaking the analysis given in lecture --- to ensure that it runs in a reasonable amount of time.) A third approach is via backtracking. In lecture we mentioned this approach only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, for example, for more details.
"""

import random
import math
from collections import defaultdict
def dataReader(filePath):
	with open(filePath) as f:
		data = f.readlines()

	numVariable = int(data[0])
	clauses = {}
	for i in range(1, len(data)):
		clauses[i] = tuple(map(int, data[i].split()))

	return numVariable, clauses


def optimization(numVariable, clauses):
	while True:
		varInfo = {}		# None - True & False, [True/False, []] - only True/False with corresponding clauses
		varDelete = set()

		for i in range(1, numVariable + 1):
			if i in clauses:
				x1, x2 = clauses[i]

				for x in [x1, x2]:
					absX = abs(x)
					if absX not in varInfo:
						varInfo[absX] = [bool(x > 0), [i]]
						varDelete.add(absX)
					elif varInfo[absX] and not (varInfo[absX][0] ^ (x > 0)):
						varInfo[absX].append(i)
					else:
						varInfo[absX] = None
						varDelete.discard(absX)

		print("delete {} variables".format(len(varDelete)))
		if not len(varDelete): break

		for x in varDelete:
			for c in varInfo[x][1]:
				if c in clauses:
					del clauses[c]

	var = set()
	optClausesList = []
	for c in clauses:
		if clauses[c]:
			var.add(abs(clauses[c][0]))
			var.add(abs(clauses[c][1]))
			optClausesList.append(c)

	return len(var), clauses, optClausesList


def check(x1, x2, clause):
	if clause[0] < 0: x1 = not x1
	if clause[1] < 0: x2 = not x2

	return x1 or x2


def Papadimitriou(numVariable, optNumVariable, clauses, optClausesList):
	if not optNumVariable: return True

	for i in range(math.ceil(math.log(optNumVariable, 2))):
		print("Num ", i)

		state = [bool(random.randint(0, 1)) for _ in range(numVariable + 1)]

		repeatTime = 2 * optNumVariable ** 2
		for j in range(repeatTime):
			if j % (repeatTime // 10) == 0: print("j = ", j)

			index = random.randint(0, len(optClausesList) - 1)

			# check current state
			findResult = True
			for _ in range(len(optClausesList)):
				cluase = optClausesList[index]
				if cluase in clauses:
					x = list(map(abs, clauses[cluase]))
					if not check(state[x[0]], state[x[1]], clauses[cluase]):
						changeVariable = x[random.randint(0, 1)]
						state[changeVariable] = not state[changeVariable]
						findResult = False
						break

				index += 1
				index %= len(optClausesList)

			if findResult: return True

	return False
		


def main():
	filePaths = ["data/2sat{}.txt".format(i) for i in range(1, 7)]
	# True, False, True, True, False, False
	
	for filePath in filePaths:
		print("==================")
		print(filePath)
		numVariable, clauses = dataReader(filePath)
		optNumVariable, clauses, optClausesList = optimization(numVariable, clauses)
		print("reduced variables: {}, reduced clauses: {}".format(optNumVariable, len(optClausesList)))
		print("ans = ", Papadimitriou(numVariable, optNumVariable, clauses, optClausesList))

	
if __name__ == "__main__":
	main()
