"""
1.Question 1
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

The file (dijkstraData.txt) contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex vv and vertex 1, we'll define the shortest-path distance between 1 and vv to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""

########################################################
# Reading the data, store the number of nodes
file = open("data/dijkstraData.txt", "r")
data = file.readlines()

num_nodes = len(data)


########################################################
# Class definition, including methods ReadingData and Dijkstra Algorithm
class Graph(object):
    def __init__(self, value):
        self.num_nodes = value
        self.graph = [[] for i in range(value+1)]
        self.arc_length = [[] for i in range(value + 1)]
        self.shortest_path_distance = [None for i in range(value+1)]

        self.__visited = [False] * (value+1)
        self.__visited[0] = True  # we don't use the 0 index of visited list

    def ReadingData(self, data):
        for line in data:
            items = line.split()

            for i in range(1, len(items)):
                self.graph[int(items[0])] += [int(items[i].split(',')[0])]
                self.arc_length[int(items[0])] += [int(items[i].split(',')[1])]

    def Dijkstra(self, source: int):
        self.shortest_path_distance[source] = 0
        self.__visited[source] = True

        while self.__visited != [True for i in range(self.num_nodes+1)]:

            min_temp = 1000000
            next_node = None

            # find vertices explored as a tail
            for v in range(1, self.num_nodes+1):
                if self.__visited[v]:

                    # find vertices not explored as a head
                    for w in self.graph[v]:
                        if not self.__visited[w]:

                            # find the position of w related to v in graph[v]
                            for i in range(len(self.graph[v])):
                                if self.graph[v][i] == w:
                                    w_index = i

                            # calculate the dijkstra value and find the minimum
                            distance = self.shortest_path_distance[v] + self.arc_length[v][w_index]
                            if distance < min_temp:
                                min_temp = distance
                                next_node = w

            # if the search is finished but there are still unexplored vertices, mark the distance as 1000000
            if min_temp == 1000000:
                for i in range(1, self.num_nodes+1):
                    if not self.__visited[i]:
                        self.__visited[i] = True
                        self.shortest_path_distance[i] = 1000000

                break

            # add next node into the list
            self.__visited[next_node] = True
            self.shortest_path_distance[next_node] = min_temp


########################################################
# Using Dijkstra Algorithm to calculate the shortest path distance from source 1
g = Graph(num_nodes)
g.ReadingData(data)
g.Dijkstra(1)
answer = g.shortest_path_distance
