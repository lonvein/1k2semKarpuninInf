def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)

def count_connected_components(N, M, edges):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * N
    count = 0 
    for u in range(N):
        if not visited[u]:
            dfs(u, graph, visited)
            count += 1
    return count
N = int(input())
M = int(input())
edges = [tuple(map(int, input().split())) for _ in range(M)]
print(count_connected_components(N, M, edges))