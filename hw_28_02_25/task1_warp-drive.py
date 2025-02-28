def has_negative_cycle(V, E, edges):
    dist = [float('inf')] * V
    dist[0] = 0  
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            return True 
    return False

s = int(input())
ans = []
for i in range(s):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    if has_negative_cycle(V, E, edges):
        ans.append('Возможно')
    else:
        ans.append("Неозможно")
for i in ans:
    print(i)