"""
1.Question 1
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

The file (2sum.txt) contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values tt in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.
"""

import time


##################################################
# Reading file
file = open("data/2sum.txt", "r")
data = file.readlines()

for i in range(len(data)):
    data[i] = int(data[i])

##################################################
# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive)
# such that there are distinct numbers x, y in the input file that satisfy x + y = t.
tic = time.time()

Dict2Sum = {}
List2Sum = []
ans_list = []
num_ans = 0

for i in data:
    Dict2Sum[i] = i
    List2Sum.append(i)

for t in range(-10000, 10001):
    for i in List2Sum:
        if t - i in Dict2Sum.keys():
            ans_list.append(t)
            num_ans += 1
            print("find x={}, y={}, t={}".format(i, t-i, t))
            break

toc = time.time()
duration = toc - tic        # 6892.771441221237

print(num_ans)              # 427
print(duration)             # 6892.771441221237
