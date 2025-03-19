def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
        return False
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1
    return True

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w, i))

edges_sorted = sorted(edges, key=lambda x: x[2])

parent = list(range(n + 1))
rank = [1] * (n + 1)

mst_edges = []
total_weight = 0
for u, v, w, idx in edges_sorted:
    if union(parent, rank, u, v):
        mst_edges.append((u, v, w, idx))
        total_weight += w

graph = [[] for _ in range(n + 1)]
for u, v, w, idx in mst_edges:
    graph[u].append((v, w, idx))
    graph[v].append((u, w, idx))

parent_tree = [0] * (n + 1)
depth = [0] * (n + 1)
max_edge = [0] * (n + 1)

def dfs(u, p):
    parent_tree[u] = p
    for v, w, idx in graph[u]:
        if v != p:
            depth[v] = depth[u] + 1
            max_edge[v] = (w, idx)
            dfs(v, u)

dfs(1, -1)

def find_max_edge(u, v):
    max_w = 0
    max_idx = -1
    while u != v:
        if depth[u] > depth[v]:
            if max_edge[u][0] > max_w:
                max_w, max_idx = max_edge[u]
            u = parent_tree[u]
        else:
            if max_edge[v][0] > max_w:
                max_w, max_idx = max_edge[v]
            v = parent_tree[v]
    return max_w, max_idx

result = [0] * m
for u, v, w, idx in edges:
    in_mst = False
    for u_mst, v_mst, w_mst, idx_mst in mst_edges:
        if (u == u_mst and v == v_mst) or (u == v_mst and v == u_mst):
            in_mst = True
            break
    if in_mst:
        result[idx] = total_weight
    else:
        max_w, max_idx = find_max_edge(u, v)
        result[idx] = total_weight - max_w + w

for res in result:
    print(res)
