N, M, *rest = map(int, input().split())
centers = rest[:len(rest) - M * 3]
roads = rest[len(rest) - M * 3:]

graph = [[] for _ in range(N)]
for i in range(M):
    u, v, w = roads[i * 3], roads[i * 3 + 1], roads[i * 3 + 2]
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start):
    dist = [float('inf')] * N
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        current_dist, u = heap.pop(0)
        if current_dist > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heap.append((dist[v], v))
                heap.sort()
    return dist

center_distances = []
for center in centers:
    dist = dijkstra(center)
    center_distances.append(dist)

total_distance = 0
for city in range(N):
    min_dist = float('inf')
    for i in range(len(centers)):
        if center_distances[i][city] < min_dist:
            min_dist = center_distances[i][city]
    if min_dist != float('inf'):
        total_distance += min_dist

print(total_distance)