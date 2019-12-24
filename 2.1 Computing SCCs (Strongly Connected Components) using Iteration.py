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
