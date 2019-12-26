class MinHeapForDijkstra(object):
    """
    This heap stores not only the values, but also their indexes, in order to store the information of the node indexes.

    """
    heap = []  # heap list
    index = []  # index list

    def __init__(self):
        self.heap = []
        self.index = []

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        self.index[index1], self.index[index2] = self.index[index2], self.index[index1]

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

    def push(self, index, value):
        """
        Push a value into the heap and rebalance the tree.

        Args:
            index: input index to represent the node index
            value: input value for pushing

        """
        # add the new value to the tail of the list
        self.heap.append(value)
        self.index.append(index)

        # bubble up to update the heap
        self.__bubble_up()

        self.check()

    def pop(self):
        """
        Pop the minimum of the heap, and rebalance the tree.
        Returns:
            min_index: the corresponding index of the minimum in the heap
            min_value: the minimum of the heap

        """
        # swap the first value and the last value
        self.__swap(0, -1)

        # pop the list to get the minimum for later return
        min_value = self.heap.pop()
        min_index = self.index.pop()

        # bubble down to update the heap
        self.__bubble_down()

        self.check()

        return min_index, min_value

    def delete(self, heap_index):
        """
        Delete the certain value/index pair (according to the heap index) in the heap, and rebalance the tree.

        Args:
            heap_index: delete the certain value/index pair of the input heap index

        """
        self.__swap(heap_index, -1)
        self.heap.pop()
        self.index.pop()

        # if the value is the last value of the heap, no need for heapify or bubble down
        if heap_index != len(self.heap):

            # if the swapped value breaks the balance, heapify again
            if self.heap[(heap_index + 1) // 2 - 1] > self.heap[heap_index]:
                self.heapify()
            else:
                self.__bubble_down(heap_index)

        self.check()
