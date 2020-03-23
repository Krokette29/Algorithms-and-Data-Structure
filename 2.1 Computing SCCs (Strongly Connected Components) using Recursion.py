"""
1.Question 1
The file (SCC.txt) contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11^{th}11 
th
  row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
"""

import sys
sys.setrecursionlimit(400000)

########################################################
# Reading the data, find the number of nodes
file = open("testCases/SCC/input_mostlyCycles_40_3200.txt", "r")
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

# the finishing order after the first pass
finishing_order = []


########################################################
# Importing the graphs
for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]


########################################################
# DFS-Loop function definition, can be used for both first pass and second pass
def DFS_Loop(G: list, order: list, cal_order=False, cal_scc=False):
    for node in order:
        if not visited[node]:
            # print('explore node {}'.format(node))
            DFS(G, node, node, cal_order, cal_scc)


def DFS(G: list, node: int, leader: int, cal_order: bool, cal_scc: bool):
    global visited
    global finishing_order
    global scc

    visited[node] = True

    if cal_scc:
        scc[leader] += 1

    for head in G[node]:
        if not visited[head]:
            DFS(G, head, leader, cal_order, cal_scc)

    if cal_order:
        finishing_order.append(node)


########################################################
# Kosaraju's Two-Pass Algorithm

# first pass: do DFS_Loop on reversed graph and calculate the finishing time, in a descend order
DFS_Loop(r_gr, reversed([i for i in range(1, num_nodes+1)]), cal_order=True)

# reset the visited list
visited = [False] * (num_nodes + 1)

# second pass: do DFS_Loop on the original graph and calculate scc
DFS_Loop(gr, reversed(finishing_order), cal_scc=True)


########################################################
# getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:5])
