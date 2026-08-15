import heapq

def a_star(graph,start,goal,h):

    pq = [(h[start],start)]
    g = {start:0}
    parent = {start:None}
    visited = set()

    while pq:

        f,node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []

            while node:
                path.append(node)
                node = parent[node]

            return path[::-1] , g[goal]

        for next,cost in graph[node]:
            new_g = g[node] + cost
            if next not in g or new_g < g[next]:
                g[next] = new_g
                parent[next] = node
                heapq.heappush(pq,(g[next]+h[next],next))

    return None



graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 5), ('D', 3)],
    'D': [('G', 3)],
    'G': []
}

h = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'G': 0
}

path, cost = a_star(graph, 'S', 'G', h)

print("Path:", path)
print("Cost:", cost)


        