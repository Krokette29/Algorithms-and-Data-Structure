"""
Consider the first, middle, and final elements of the given array. 
(If the array has odd length it should be clear what the "middle" element is; 
for an array with even length 2k, use the k^{th} element as the "middle" element. 
So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) 
Identify which of these three elements is the median 
(i.e., the one whose value is in between the other two), and use this as your pivot.

EXAMPLE: For the input array 8 2 4 5 7 1 
you would consider the first (8), middle (4), and last (1) elements; 
since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.
"""

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

	# Preprocessing of median-of-three
	# ------Way 1------
	# n = r - l + 1
	# c1 = A[l] > A[(l+r)//2]
	# c2 = A[l] > A[r]
	# c3 = A[(l+r)//2] > A[r]
	# if (c1 and c2 and c3) or (not (c1 or c2 or c3)):
	# 	A[l], A[(l+r)//2] = A[(l+r)//2], A[l]
	# elif (c1 and c2 and (not c3)) or (not (c1 or c2 or (not c3))):
	# 	A[l], A[r] = A[r], A[l]

	# ------Way 2------
	# middelNum = sorted([A[l], A[(l+r)//2], A[r]])[1]
	# if A[(l+r)//2] == middelNum:
	# 	A[l], A[(l+r)//2] = A[(l+r)//2], A[l]
	# elif A[r] == middelNum:
	# 	A[l], A[r] = A[r], A[l]

	# ------Way 3------
	middelNum = sum([A[l], A[(l+r)//2], A[r]]) - max([A[l], A[(l+r)//2], A[r]]) - min([A[l], A[(l+r)//2], A[r]])
	if A[(l+r)//2] == middelNum:
		A[l], A[(l+r)//2] = A[(l+r)//2], A[l]
	elif A[r] == middelNum:
		A[l], A[r] = A[r], A[l]

	# Partition part
	p = A[l]
	i = l + 1
	for j in range(l + 1, r + 1):
		if A[j] < p:
			A[j], A[i] = A[i], A[j]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]

	# print("middel:", A)

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

	numList, cpNum = QuickSort(numList, 0, len(numList)-1)
	# print("The sorted number list is:\n", numList)
	print("The number of comparisons is:\n", cpNum)
	print("(Using median of three numbers as pivot)")

if __name__ == "__main__":
	main()