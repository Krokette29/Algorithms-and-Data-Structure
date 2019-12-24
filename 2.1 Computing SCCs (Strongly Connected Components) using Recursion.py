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
