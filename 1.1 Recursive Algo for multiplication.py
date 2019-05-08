import time

def listToInt(name):
	'''
	Convert a list to a number type.
	'''
	num = ''
	for i in name:
		num = num + str(i)
	return int(num)


def strToList(name):
	'''
	Convert a string to a list type.
	'''
	listAns = []
	for i in name:
		listAns.append(int(i))
	return listAns




def karatsuba_rec(x, y):
	# x, y - int
	x_list = strToList(str(x))
	y_list = strToList(str(y))

	n = len(x_list)
	if n == 1:
		return x_list[0] * y_list[0]

	a_list = x_list[:int(n/2)]
	b_list = x_list[int(n/2):]
	c_list = y_list[:int(n/2)]
	d_list = y_list[int(n/2):]

	ac = karatsuba_rec(listToInt(a_list), listToInt(c_list))
	bd = karatsuba_rec(listToInt(b_list), listToInt(d_list))
	ad = karatsuba_rec(listToInt(a_list), listToInt(d_list))
	bc = karatsuba_rec(listToInt(b_list), listToInt(c_list))

	# gaussNum = karatsuba_rec(listToInt(a_list)+listToInt(b_list), listToInt(c_list)+listToInt(d_list)) - ac - bd

	return int(10**n*ac + 10**(n/2)*(ad + bc) + bd)




input1 = input('input1:')
input2 = input('input2:')

time.process_time()

x = listToInt(strToList(input1))
y = listToInt(strToList(input2))

myAnswer = karatsuba_rec(x, y)
exactAnswer = x * y
print('My answer:' + str(myAnswer))
print('Exact answer:' + str(exactAnswer))

error = myAnswer - exactAnswer
print('Error:' + str(error))

print('Running Time: {:.3}s'.format(time.process_time()))