"""
1.Question 1
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

The file (dijkstraData.txt) contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex vv and vertex 1, we'll define the shortest-path distance between 1 and vv to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""

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
