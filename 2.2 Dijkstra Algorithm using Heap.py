from MinHeapForDijkstra import *

########################################################
# Reading the data, store the number of nodes
file = open("data/dijkstraData.txt", "r")
data = file.readlines()

num_nodes = len(data)


########################################################
# Class definitions
class Node(object):
    next_node = {}      # use a dictionary to store the information of the next nodes (index and distance)

    def __init__(self):
        self.next_node = {}

    def add_next_distance(self, next_node_index, next_node_distance):
        self.next_node[next_node_index] = next_node_distance


class Graph(object):
    num_nodes = 0                                       # the number of total nodes
    graph = [Node() for i in range(num_nodes + 1)]      # list of Node objects, index of graph represents index of nodes

    # store the information of shortest path distances (from source), index represents the index of nodes
    shortest_path_distance = [None for i in range(num_nodes + 1)]

    def __init__(self, value):
        self.num_nodes = value
        self.graph = [Node() for i in range(value + 1)]  # we don't use index 0
        self.shortest_path_distance = [None for i in range(value + 1)]

    def ReadingData(self, data):
        """
        Reading data into the Graph, store in self.graph
        Args:
            data: input data of graph information (stored in list for every node)

        """
        for line in data:
            items = line.split()
            for i in range(1, len(items)):
                next_node_index = int(items[i].split(',')[0])
                next_node_distance = int(items[i].split(',')[1])
                self.graph[int(items[0])].add_next_distance(next_node_index, next_node_distance)

    def Dijkstra(self, source: int):
        """
        Use Dijkstra Algorithm to find the shortest path distance for every node from source

        Args:
            source: the source index

        """
        self.shortest_path_distance[source] = 0

        visited = [False] * (self.num_nodes + 1)
        visited[0] = True  # we don't use index 0
        visited[source] = True

        # initialize the heap for storing the minimum of Dijkstra values
        heap = MinHeapForDijkstra()

        # last_node represents the last explored node
        last_node = source

        while visited != [True for i in range(self.num_nodes + 1)]:

            # UPDATE HEAP PROCEDURE
            # loop over the head vertices of last_node in the unexplored area
            for w in self.graph[last_node].next_node.keys():
                if not visited[w]:

                    # calculate the Dijkstra value
                    dijkstra_value = self.shortest_path_distance[last_node] + self.graph[last_node].next_node[w]

                    # if w not in the index list of the heap, add it
                    if w not in heap.index:
                        heap.push(w, dijkstra_value)

                    # if w in the index list of the heap, compare with the old value
                    else:
                        # find the heap index of w in the heap, in order to retrieve the corresponding value in the heap
                        heap_index = None
                        for i in range(len(heap.heap)):
                            if heap.index[i] == w:
                                heap_index = i
                                break

                        # if the new Dijkstra value is smaller, update it; otherwise do nothing
                        if dijkstra_value < heap.heap[heap_index]:
                            heap.delete(heap_index)
                            heap.push(w, dijkstra_value)

            # pop the heap and add the next node into the explored area, update shortest_path_distance
            try:
                next_node, next_node_distance = heap.pop()
                self.shortest_path_distance[next_node] = next_node_distance
                visited[next_node] = True
                last_node = next_node

            # if the heap is empty, means the search is finished, mark the rest vertices as 1000000
            except IndexError:
                for i in range(1, self.num_nodes+1):
                    if not visited[i]:
                        visited[i] = True
                        self.shortest_path_distance[i] = 1000000


########################################################
# Using Dijkstra Algorithm to calculate the shortest path distance from source 1
g = Graph(num_nodes)
g.ReadingData(data)
g.Dijkstra(1)
answer = g.shortest_path_distance

print(answer[1:31])
