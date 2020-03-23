"""
1.Question 1
The file (SCC.txt) contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11^{th}11 
th
  row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
"""

########################################################
# Reading the data, find the number of nodes
file = open("data/SCC.txt", "r")
data = file.readlines()

num_nodes = 0

# first traverse the data, find the number of nodes
for line in data:
    items = line.split()
    for i in range(2):
        if int(items[i]) > num_nodes:
            num_nodes = int(items[i])


########################################################
# Data structures

# adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes+1)]
r_gr = [[] for i in range(num_nodes+1)]

# list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * (num_nodes + 1)

# list index represents the scc leader, and the value is the size of the scc
scc = [0] * (num_nodes + 1)

# stack for DFS
stack = []

# the finishing order after the first pass
finishing_order = []

# temporary order list for every leader in the first pass
order_temp = []


########################################################
# Importing the graphs
for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]


########################################################
# DFS on reverse graph
for node in [i for i in range(num_nodes+1)]:
    if not visited[node]:
        stack.append(node)
        visited[node] = True
        order_temp.append(node)

        while stack:
            stack_node = stack.pop()

            for head in r_gr[stack_node]:
                if not visited[head]:
                    stack.append(head)
                    visited[head] = True
                    order_temp.append(head)

        # reverse order_temp and add to finishing_order, in order to be sure that the finishing order is correct
        order_temp.reverse()
        finishing_order += order_temp
        order_temp = []


########################################################
# DFS on original graph
visited = [False] * len(visited)  # Resetting the visited variable
finishing_order.reverse()  # The nodes should be visited in reverse finishing times

for node in finishing_order:

    # if node is not visited, then it becomes a leader
    if not visited[node]:
        stack.append(node)
        visited[node] = True
        scc[node] += 1  # leader nodes are also part of the sccs

        while stack:
            stack_node = stack.pop()

            for head in gr[stack_node]:
                if not visited[head]:
                    stack.append(head)
                    visited[head] = True
                    scc[node] += 1


########################################################
# Getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:10])
