# Input===========================
ve = input("Input Vertex and Edge number: ")
l1 = ve.split()
vertex = l1[0]
edge = l1[1]

sg = input("Input Start and Goal node: ")
l2 = sg.split()
start = l2[0]
goal = l2[1]

heuristic = {}
for i in range (int(vertex)):
    heu = input("Input Vertex with Heurisitc value: ")
    l3 = heu.split()

    heuristic[l3[0]] = l3[1]

graph = {}
for i in range (int(edge)):
    connection = input("Input vertex connection: ")
    l4 = connection.split()

    v = l4[0] # Creating the graph backward to start bfs from goal node
    u = l4[1]

    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    
    if v not in graph:
        graph[v] = []
    graph[v].append(u)




# Admissibility checking function=====================================

def admissible(graph, heuristic,initial,end):

    start = end
    goal = initial # traverse the graph from back

    path_cost = {} # From ending node to certain node (bfs from back)

    # BFS
    q = deque()
    visited = set()

    q.append(start)
    visited.add(start)
    path_cost[start] = 0


    while q:
        elem = q.popleft()

        for i in graph[elem]:
            if i not in visited:
                visited.add(i)
                q.append(i)
                path_cost[i] = path_cost[elem] + 1

    # Checking admissibility
    inadmissible = []

    for key,value in heuristic.items():

        if key in path_cost:
            if int(value) > int(path_cost[key]):
                inadmissible.append(key)

    if len(inadmissible) == 0:
        print(1)
    else:
        print(0)
        print("Inadmissible Nodes:")
        for i in inadmissible:
            print(i)

        

# Function calling===================================================

from collections import deque
admissible(graph, heuristic,start,goal)


# Sample INPUT and OUTPUT=============================================
# Input Sample 
# 6 7   //vertex edge count
# 1 6   //initial,goal
# 1 3   //heuristic
# 2 2
# 3 1
# 4 2
# 5 1
# 6 0
# 1 2   //node connections
# 2 3
# 3 6
# 1 4
# 4 5
# 5 6
# 3 5

# Output Sample 
# 1
# As the heuristic values are admissible.
