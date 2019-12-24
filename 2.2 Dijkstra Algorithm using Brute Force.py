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
