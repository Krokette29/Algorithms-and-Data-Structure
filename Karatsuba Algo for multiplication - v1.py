import time

def zeroPad(numStr, zeroNum):
	'''
	Add zeroNum zeros at the end of numStr.

	input - string, int
	output - string
	'''
	for i in range(zeroNum):
		numStr = numStr + '0'

	return numStr

def karatsuba_rec(x, y):
	'''
	
	'''
	x = str(x)
	y = str(y)

	# x, y - string

	n = len(x)
	if n == 1:
		return int(x) * int(y)

	a = int(x[:int(n/2)])
	b = int(x[int(n/2):])
	c = int(y[:int(n/2)])
	d = int(y[int(n/2):])

	# a, b, c, d - int

	ac = karatsuba_rec(a, c)
	bd = karatsuba_rec(b, d)
	ad = karatsuba_rec(a, d)
	bc = karatsuba_rec(b, c)

	# gaussNum = karatsuba_rec(a+b, c+d)

	return int(zeroPad(str(ac), n)) + int(zeroPad(str(ad + bc), int(n/2))) + bd


x = input('input1:')
y = input('input2:')

time.process_time()

myAnswer = karatsuba_rec(x, y)
exactAnswer = int(x) * int(y)
print('My answer:' + str(myAnswer))
print('Exact answer:' + str(exactAnswer))

error = myAnswer - exactAnswer
print('Error:' + str(error))

print('Running Time: {:.3}s'.format(time.process_time()))