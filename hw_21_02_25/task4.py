def dijkstra(V, E, start, end, edges):
    INF = float('inf')
    dist = {station: INF for station in V}
    dist[start] = 0
    prev = {station: None for station in V}
    visited = set()
    while len(visited) < len(V):
        u = min((station for station in V if station not in visited), key=lambda x: dist[x])
        visited.add(u)
        if u == end:
            break
        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return dist[end], path
V_E_start_end = input().split()
V = int(V_E_start_end[0])
E = int(V_E_start_end[1])
start = V_E_start_end[2]
end = V_E_start_end[3]
edges = {}
stations = set()
for _ in range(E):
    name_1, name_2, time = input().split()
    time = int(time)
    stations.add(name_1)
    stations.add(name_2)
    if name_1 not in edges:
        edges[name_1] = []
    if name_2 not in edges:
        edges[name_2] = []
    edges[name_1].append((name_2, time))
    edges[name_2].append((name_1, time))
min_time, path = dijkstra(stations, E, start, end, edges)
print(min_time)
with open("path.txt", "w") as f:
    f.write(" -> ".join(path))
print("Кратчайший путь:", " -> ".join(path))