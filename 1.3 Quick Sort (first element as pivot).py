def QuickSort(A, l, r):
	"""
	Arguments:
	A -- total number list
	l -- left index of input list
	r -- right index of input list

	Returns:
	ASorted -- sorted list
	cpNum -- Number of comparisons
	"""

	# Number of comparisons
	cpNum = r - l

	# Base case
	if cpNum == 0:
		return [A[l]], 0
	elif cpNum < 0:
		return [], 0

	# Partition part
	p = A[l]
	i = l + 1
	for j in range(l + 1, r + 1):
		if A[j] < p:
			A[j], A[i] = A[i], A[j]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]

	# Recursion call
	ALeft, cpNumLeft = QuickSort(A, l, i-2)
	ARight, cpNumRight = QuickSort(A, i, r)
	ASorted = ALeft + [p] + ARight
	cpNum = cpNum + cpNumLeft + cpNumRight

	return ASorted, cpNum

def main():
	numList = []
	with open('data/QuickSort.txt', 'r') as f:
	    while True:
	        line = f.readline().strip()
	        if not line:
	            break
	        numList.append(int(line))

	# numList = [1, 3, 5, 2, 4, 6]

	numList, cpNum = QuickSort(numList, 0, len(numList)-1)
	# print("The sorted number list is:\n", numList)
	print("The number of comparisons is:\n", cpNum)
	print("(Using first element as pivot)")

if __name__ == "__main__":
	main()