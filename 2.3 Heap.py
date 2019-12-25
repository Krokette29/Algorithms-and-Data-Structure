import math


class MinHeap(object):
    heap = []       # heap list
    num_layer = 0       # number of layers

    def __init__(self, unsorted_list: list):
        self.heap = []

        for i in range(len(unsorted_list)):
            # add the next entry into heap
            self.heap.append(unsorted_list[i])
            self.__bubble_up()

        # calculate the number of layers for use of drawing the heap tree
        self.__calculate_num_layer()

    def __calculate_num_layer(self):
        self.num_layer = math.ceil(math.log(len(self.heap), 2))

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __bubble_up(self):
        # i is the tail index of the list
        i = len(self.heap) - 1

        while i != 0:
            # if the child node smaller than parent node, swap them
            if self.heap[(i + 1) // 2 - 1] > self.heap[i]:
                self.__swap((i + 1) // 2 - 1, i)
                i = (i + 1) // 2 - 1
            else:
                break

    def __bubble_down(self):
        i = 0
        while True:
            # in this case, the node has two children
            try:
                # decide with which child to swap, if necessary
                if self.heap[2 * (i + 1) - 1] < self.heap[2 * (i + 1)]:
                    if self.heap[i] > self.heap[2 * (i + 1) - 1]:
                        self.__swap(i, 2 * (i + 1) - 1)
                        i = 2 * (i + 1) - 1
                    else:
                        break
                else:
                    if self.heap[i] > self.heap[2 * (i + 1)]:
                        self.__swap(i, 2 * (i + 1))
                        i = 2 * (i + 1)

            # in this case, the node has only one child
            except IndexError:
                try:
                    if self.heap[i] > self.heap[2 * (i + 1) - 1]:
                        self.__swap(i, 2 * (i + 1) - 1)
                        i = 2 * (i + 1) - 1
                    else:
                        break

                # in this case, the node has no children, stop the procedure
                except IndexError:
                    break

    def get_heap(self):
        return self.heap

    def push(self, value):
        # add the new value to the tail of the list
        self.heap.append(value)

        # bubble up to update the heap
        self.__bubble_up()
        self.__calculate_num_layer()

    def pop(self):
        # swap the first value and the last value
        self.__swap(0, -1)

        # pop the list to get the minimum for later return
        min_value = self.heap.pop()

        # bubble down to update the heap
        self.__bubble_down()

        return min_value

    def print_heap(self):
        print(self.heap)

    def draw_heap(self, num_tab: int = 1):
        # print every layer
        for i in range(self.num_layer):
            string = ''
            for j in range(2**i):
                try:
                    string += str(self.heap[2**i+j-1])
                    string += '\t' * num_tab * 2**(self.num_layer - i - 1)
                except IndexError:
                    break
            print(string)


test_list = [6, 5, 4, 1, 7, 3, 2]
test_heap = MinHeap(test_list)

test_heap.print_heap()
test_heap.draw_heap()

print('')
print("min is {}".format(test_heap.pop()))
test_heap.print_heap()
test_heap.draw_heap()
