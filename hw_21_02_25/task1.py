def dijkstra(n, m, s, f, edges):
    INF = float('inf')
    dist = [INF] * n 
    dist[s] = 0       
    visited = [False] * n 
    prev = [-1] * n   
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) 
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == INF:
            break
        visited[u] = True 
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
    path = []
    current = f
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return len(path), path
n, m, s, f = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
length, path = dijkstra(n, m, s, f, edges)
print(length)
