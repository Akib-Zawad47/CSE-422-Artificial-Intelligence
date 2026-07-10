# Input Section============================================

text = []

print("Input Your Text and Press Enter Twice")
while True:
    line = input()
    if line == "":
        break
    text.append(line)

start = input("Insert starting node: ")
goal = input("Insert destination node: ")

# Processing input=========================================

heuristic = {}
graph = {}

for i in text:
    line = i.split()

    heuristic[line[0]] = int(line[1])

    graph[line[0]] = [] # Initializing key with empty list to append the elements
    
    for connection in range(2,len(line),2):
        graph[line[0]].append((line[connection],int(line[connection+1]))) # tuple = (destination,cost)



# A_Star Code==============================================
import heapq

def a_star(graph,heuristic,start,goal):
    q = [(0,start)] # short based on first element of tuple
    parent={start: None}
    g_cost={start:0}

    while q:
        f,current = heapq.heappop(q)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            
            #Printing path and total distance
            path.reverse()
            s = ""
            for i in path:
                if i == start:
                    s = s + i
                else:
                    s = s + " -> " + str(i)

            total_distance = g_cost[goal]
        
            return f"Path: {s}\nTotal DIstance: {total_distance} km" 
    
        for child, cost in graph[current]:
            new_g = g_cost[current] + cost

            if child not in g_cost or new_g < g_cost[child]: # Same heuristic for same node 
                g_cost[child] = new_g

                f_cost = heuristic[child] + g_cost[child]
                heapq.heappush(q,(f_cost,child))
                parent[child] = current

    return "NO PATH FOUND"



        
# Sample Input Text=============================================

# Arad 366 Zerind 75 Timisoara 118 Sibiu 140
# Craiova 160 Dobreta 120 RimnicuVilcea 146 Pitesti 138
# Eforie 161 Hirsova 86
# Fagaras 176 Sibiu 99 Bucharest 211
# Giurgiu 77 Bucharest 90
# Mehadia 241 Lugoj 70 Dobreta 75
# Neamt 234 lasi 87
# Sibiu 253 Oradea 151 Arad 140 RimnicuVilcea 80 Fagaras 99
# Oradea 380 Zerind 71 Sibiu 151
# Pitesti 100 RimnicuVilcea 97 Craiova 138 Bucharest 101
# RimnicuVilcea 193 Sibiu 80 Craiova 146 Pitesti 97
# Dobreta 242 Mehadia 75 Craiova 120
# Hirsova 151 Urziceni 98 Eforie 86
# lasi 226 Vaslui 92 Neamt 87
# Lugoj 244 Timisoara 111 Mehadia 70
# Timisoara 329 Arad 118 Lugoj 111
# Urziceni 80 Bucharest 85 Hirsova 98 Vaslui 142
# Vaslui 199 Urziceni 142 lasi 92 
# Zerind 374 Oradea 71 Arad 75
# Bucharest 0 Fagaras 211 Pitesti 101 Giurgiu 90 Urziceni 85


# Start node: Arad
# Destination: Bucharest

# Sample output
# Path: Arad -> Sibiu -> RimnicuVilcea -> Pitesti -> Bucharest
# Total distance: 418 km




# Function calling=========================================

print(a_star(graph,heuristic,start,goal))





