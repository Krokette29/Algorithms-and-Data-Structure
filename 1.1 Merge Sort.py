'''
Merge Sort using Devide and Conquer.
Time complexity using Master Method:
T(n) <= 2T(n/2) + O(n) = O(nlogn)
'''

import time

def mergeSort(listNum):
	# the base situation
	if len(listNum) == 1:
		return listNum

	# devide listNum into two lists
	listA = listNum[:len(listNum)//2]
	listB = listNum[len(listNum)//2:]

	# recursivly sort listA and listB
	listA_sorted = mergeSort(listA)
	listB_sorted = mergeSort(listB)

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
			if j == len(listB_sorted):
				j = j - 1
				flag = 1

	return listC


inputUsr = input('Please input numbers using space:')

time.process_time()
# seperate the input into a list of number
listNum = inputUsr.split()
for i in range(len(listNum)):
	listNum[i] = int(listNum[i])

print('The origin list of numbers:{}'.format(listNum))
print('The sorted list of numbers:{}'.format(mergeSort(listNum)))
print('Running time: {:.2}s'.format(time.process_time()))