def bfs_distances(n, m, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    distances = [-1] * n  
    distances[0] = 0      
    queue = []
    queue.append(0)  
    while queue:
        u = queue.pop(0) 
        for v in graph[u]:
            if distances[v] == -1:  #
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
distances = bfs_distances(n, m, edges)
for dist in distances:
    print(dist)