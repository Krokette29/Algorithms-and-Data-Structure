'''
Multiplication using Karatsuba Algorithm.
Input two integers, no matter how long they respectivly are.
Quite perfect function.
T(n) <= 3T(n/2) + O(n) = O(n**(log2(3))) = O(n**1.59)
which is quite better than naiver recursive altorithm with O(n**2).
'''

import time

def karatsubaRec(x, y):
	x = str(x)
	y = str(y)

	# x, y - string

	# initialize length list of x and y
	n = [0, 0]

	n[0] = len(x)
	n[1] = len(y)
	if n[0] == 1 or n[1] == 1:
		return int(x) * int(y)

	flag = 0
	# devide process
	if n[0] < n[1]:
		nDevide = n[0]//2
		a = int(x[:nDevide])
		b = int(x[nDevide:])
		c = int(y[:(n[1] - n[0] + nDevide)])
		d = int(y[(n[1] - n[0] + nDevide):])
	else:
		# flag is used in 'return'
		flag = 1
		nDevide = n[1]//2
		a = int(x[:(n[0] - n[1] + nDevide)])
		b = int(x[(n[0] - n[1] + nDevide):])
		c = int(y[:nDevide])
		d = int(y[nDevide:])	

	# a, b, c, d - int

	# three recursive calls
	ac = karatsubaRec(a, c)
	bd = karatsubaRec(b, d)
	gaussNum = karatsubaRec(a+b, c+d) - ac - bd

	return int(zeroPad(str(ac), 2 * (n[0+flag] - nDevide))) + int(zeroPad(str(gaussNum), (n[0+flag] - nDevide))) + bd


def zeroPad(numStr, zeroNum):
	'''
	Add zeroNum zeros at the end of numStr.

	input - string, int
	output - string
	'''
	for i in range(zeroNum):
		numStr = numStr + '0'

	return numStr


x = input('input1:')
y = input('input2:')

# start the timer
time.process_time()

myAnswer = karatsubaRec(x, y)
exactAnswer = int(x) * int(y)
print('My answer:' + str(myAnswer))
print('Exact answer:' + str(exactAnswer))

error = myAnswer - exactAnswer
print('Error:' + str(error))

# calculate the running time
print('Running Time: {:.3}s'.format(time.process_time()))