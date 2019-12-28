import math
from io import StringIO


class MinHeap(object):
    heap = []               # heap list
    check_flag = False      # True for running the checking code

    def __init__(self, unsorted_list: list, check_flag=False):
        self.heap = unsorted_list
        self.check_flag = check_flag

        # heapify the unsorted list
        self.heapify()

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

    def __bubble_down(self, index: int = 0):
        # if there is no input value, then bubble down from top
        while True:
            # in this case, the node has two children
            try:
                # decide with which child to swap, if necessary
                if self.heap[2 * (index + 1) - 1] < self.heap[2 * (index + 1)]:
                    if self.heap[index] > self.heap[2 * (index + 1) - 1]:
                        self.__swap(index, 2 * (index + 1) - 1)
                        index = 2 * (index + 1) - 1
                    else:
                        break
                else:
                    if self.heap[index] > self.heap[2 * (index + 1)]:
                        self.__swap(index, 2 * (index + 1))
                        index = 2 * (index + 1)
                    else:
                        break

            # in this case, the node has only one child
            except IndexError:
                try:
                    if self.heap[index] > self.heap[2 * (index + 1) - 1]:
                        self.__swap(index, 2 * (index + 1) - 1)
                        index = 2 * (index + 1) - 1
                    else:
                        break

                # in this case, the node has no children, stop the procedure
                except IndexError:
                    break

    def check(self):
        """
        Check if the heap is still balance.

        """
        if self.check_flag:
            for i in range(1, len(self.heap)):
                if self.heap[(i + 1) // 2 - 1] > self.heap[i]:
                    print('-----Error List-----')
                    print(self.heap)
                    print('-----Error Value-----')
                    print('{} : {}'.format(self.heap[(i + 1) // 2 - 1], self.heap[i]))
                    raise ValueError('Heap Error!')

    def heapify(self):
        """
        Heapify the heap to reach a balance.

        """
        original_heap = self.heap
        self.heap = []

        for i in range(len(original_heap)):
            # add the next entry into heap
            self.heap.append(original_heap[i])
            self.__bubble_up()

        self.check()

    def push(self, value):
        """
        Push a value into the heap and rebalance the tree.

        Args:
            value: input value for pushing

        """
        # add the new value to the tail of the list
        self.heap.append(value)

        # bubble up to update the heap
        self.__bubble_up()

        self.check()

    def pop(self):
        """
        Pop the minimum of the heap, and rebalance the tree.
        Returns:
            min_value: the minimum of the heap

        """
        # swap the first value and the last value
        self.__swap(0, -1)

        # pop the list to get the minimum for later return
        min_value = self.heap.pop()

        # bubble down to update the heap
        self.__bubble_down()

        self.check()

        return min_value

    def delete(self, value):
        """
        Delete the certain value in the heap, and rebalance the tree.

        Args:
            value: input value to be deleted

        """
        delete_complete = False

        # find the index of value and delete it from the heap
        for i in range(len(self.heap)):
            if value == self.heap[i]:
                self.__swap(i, -1)
                self.heap.pop()
                delete_complete = True

                # if the value is the last value of the heap, no need for heapify or bubble down
                if i == len(self.heap):
                    break

                # if the swapped value breaks the balance, heapify again
                if self.heap[(i + 1) // 2 - 1] > self.heap[i]:
                    self.heapify()
                else:
                    self.__bubble_down(i)
                break

        if not delete_complete:
            print("No such value in the heap!")

    def show_tree(self, total_width=36, fill=' '):
        """
        Draw a tree, from learnku.com - heapq

        """
        output = StringIO()
        last_row = -1

        for i, n in enumerate(self.heap):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor(total_width / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row

        print(output.getvalue())
        print('-' * total_width)
        print()


class MaxHeap(object):
    heap = []  # heap list
    check_flag = False  # True for running the checking code

    def __init__(self, unsorted_list: list, check_flag=False):
        self.heap = unsorted_list
        self.check_flag = check_flag

        # heapify the unsorted list
        self.heapify()

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __bubble_up(self):
        # i is the tail index of the list
        i = len(self.heap) - 1

        while i != 0:
            # if the child node bigger than parent node, swap them
            if self.heap[(i + 1) // 2 - 1] < self.heap[i]:
                self.__swap((i + 1) // 2 - 1, i)
                i = (i + 1) // 2 - 1
            else:
                break

    def __bubble_down(self, index: int = 0):
        # if there is no input value, then bubble down from top
        while True:
            # in this case, the node has two children
            try:
                # decide with which child to swap, if necessary
                if self.heap[2 * (index + 1) - 1] > self.heap[2 * (index + 1)]:
                    if self.heap[index] < self.heap[2 * (index + 1) - 1]:
                        self.__swap(index, 2 * (index + 1) - 1)
                        index = 2 * (index + 1) - 1
                    else:
                        break
                else:
                    if self.heap[index] < self.heap[2 * (index + 1)]:
                        self.__swap(index, 2 * (index + 1))
                        index = 2 * (index + 1)
                    else:
                        break

            # in this case, the node has only one child
            except IndexError:
                try:
                    if self.heap[index] < self.heap[2 * (index + 1) - 1]:
                        self.__swap(index, 2 * (index + 1) - 1)
                        index = 2 * (index + 1) - 1
                    else:
                        break

                # in this case, the node has no children, stop the procedure
                except IndexError:
                    break

    def check(self):
        """
        Check if the heap is still balance.

        """
        if self.check_flag:
            for i in range(1, len(self.heap)):
                if self.heap[(i + 1) // 2 - 1] < self.heap[i]:
                    print('-----Error List-----')
                    print(self.heap)
                    print('-----Error Value-----')
                    print('{} : {}'.format(self.heap[(i + 1) // 2 - 1], self.heap[i]))
                    raise ValueError('Heap Error!')

    def heapify(self):
        """
        Heapify the heap to reach a balance.

        """
        original_heap = self.heap
        self.heap = []

        for i in range(len(original_heap)):
            # add the next entry into heap
            self.heap.append(original_heap[i])
            self.__bubble_up()

        self.check()

    def push(self, value):
        """
        Push a value into the heap and rebalance the tree.

        Args:
            value: input value for pushing

        """
        # add the new value to the tail of the list
        self.heap.append(value)

        # bubble up to update the heap
        self.__bubble_up()

        self.check()

    def pop(self):
        """
        Pop the minimum of the heap, and rebalance the tree.
        Returns:
            max_value: the minimum of the heap

        """
        # swap the first value and the last value
        self.__swap(0, -1)

        # pop the list to get the minimum for later return
        max_value = self.heap.pop()

        # bubble down to update the heap
        self.__bubble_down()

        self.check()

        return max_value

    def delete(self, value):
        """
        Delete the certain value in the heap, and rebalance the tree.

        Args:
            value: input value to be deleted

        """
        delete_complete = False

        # find the index of value and delete it from the heap
        for i in range(len(self.heap)):
            if value == self.heap[i]:
                self.__swap(i, -1)
                self.heap.pop()
                delete_complete = True

                # if the value is the last value of the heap, no need for heapify or bubble down
                if i == len(self.heap):
                    break

                # if the swapped value breaks the balance, heapify again
                if self.heap[(i + 1) // 2 - 1] < self.heap[i]:
                    self.heapify()
                else:
                    self.__bubble_down(i)
                break

        if not delete_complete:
            print("No such value in the heap!")

    def show_tree(self, total_width=36, fill=' '):
        """
        Draw a tree, from learnku.com - heapq

        """
        output = StringIO()
        last_row = -1

        for i, n in enumerate(self.heap):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor(total_width / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row

        print(output.getvalue())
        print('-' * total_width)
        print()
