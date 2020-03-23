"""
1.Question 1

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,...,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,...,xk; if k is even, then mk is the (k/2)th smallest number among x1,...,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.
"""

from Heap import *
import time


########################################################
# Reading Data
file = open("data/Median.txt", "r")
data = file.readlines()


########################################################
# Median Maintenance using Heap

# record the code running time
tic = time.time()

min_heap = MinHeap([])      # MinHeap stores the larger half of the list
max_heap = MaxHeap([])      # MaxHeap stores the smaller half of the list

# change string list into int list
data = list(map(int, data))

# initialize median and the sum of median, push the first value into MinHeap
median = data[0]
median_sum = median
min_heap.push(data[0])

# the data comes in one by one
for i in range(1, len(data)):
    # decide which side the next value should go
    if data[i] > min_heap.heap[0]:
        min_heap.push(data[i])
    else:
        max_heap.push(data[i])

    # rebalance two heaps, so that they remain almost the same length
    if len(max_heap.heap) > len(min_heap.heap) + 1:
        value = max_heap.pop()
        min_heap.push(value)
    elif len(min_heap.heap) > len(max_heap.heap):
        value = min_heap.pop()
        max_heap.push(value)

    # update the sum of median, retain 4 digits
    median = max_heap.heap[0]
    median_sum += median
    if median_sum > 10000:
        median_sum -= 10000

toc = time.time()
running_time = toc - tic

print("The last 4 digits of the sum of the medians are: %s" % median_sum)
print("Running time using heap: %.2fs" % running_time)
