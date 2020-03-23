"""
1.Question 1
This file (IntegerArray.txt) contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
"""

# first try: 40405901038421, wrong!
# second try: 2397819672, wrong! mind that 'a' from txt file is a string list, not int list
# third try: 2407905288, correct! 
import time

'''
# this part is for the test cases
# input of the test cases
test = '_9_16'
input = open('./testCases/Inversions/input_beaunus{}.txt'.format(test))
a = input.readlines()
a = ''.join(a)
a = a.split()
input.close()

# output of the test cases
output = open('./testCases/Inversions/output_beaunus{}.txt'.format(test))
b = output.readline()
b = int(b)
output.close()
'''

# open the txt file, which includs 100,000 numbers in an unsorted order
input = open('data/MergeSortIntegerArray.txt')

# read the file, and split into a list
a = input.readlines()
a = ''.join(a)
a = a.split()

input.close()

# don't forget to turn the strings into int
for i in range(len(a)):
	a[i] = int(a[i])


# devide and conquer using the idea of merge sort
def CountInv(listNum):
	splitNum = 0

	# the base situation
	if len(listNum) == 1:
		return listNum, 0

	# devide listNum into two lists
	listA = listNum[:len(listNum)//2]
	listB = listNum[len(listNum)//2:]

	# recursivly sort listA and listB
	listA_sorted, splitA = CountInv(listA)
	listB_sorted, splitB = CountInv(listB)

	# initialize the output, name as listC
	listC = []

	# i - pointer in listA
	# j - pointer in listB
	# flag - end condition
	i = 0
	j = 0
	flag = 0

	# O(n) outside recursive calls
	for k in range(len(listNum)):
		if ((listA_sorted[i] < listB_sorted[j]) or flag == 1) and flag != 2:
			listC.append(listA_sorted[i])
			i = i + 1
			if i == len(listA_sorted):
				i = i - 1
				flag = 2
		else:
			listC.append(listB_sorted[j])
			j = j + 1
			if flag != 2:
				splitNum = splitNum + len(listA_sorted) - i
			if j == len(listB_sorted):
				j = j - 1
				flag = 1

	# just for debug:
	# print('splitA:{}'.format(splitA))
	# print('splitB:{}'.format(splitB))
	# print('splitNum:{}'.format(splitNum))

	return listC, splitA + splitB + splitNum


# Brute-force
def CountInvBrute(a):
	num = 0
	for i in range(len(a)-1):
		for j in range(len(a)-i-1):
			# mind that a[i] and a[j] are not the same one
			if a[i] > a[i+j+1]:
				num = num + 1
	return num


tic = time.perf_counter()
ans1 = CountInv(a)[1]
toc1 = time.perf_counter()
# ans2 = CountInvBrute(a)
# toc2 = time.perf_counter()

print('Answer by devide and conquer: {}'.format(ans1))
print('Running time: {:.4}s'.format(toc1 - tic))
# print('Answer by Brute-force: {}'.format(ans2))
# print('Running time: {}s'.format(toc2 - toc1))
# print('Exact output: {}'.format(b))
# print('Error: {}'.format(ans1 - ans2))