n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
operations = [input().split() for _ in range(k)]

parent = [i for i in range(n + 1)]
rank = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot == yroot:
        return False
    if rank[xroot] < rank[yroot]:
        xroot, yroot = yroot, xroot
    parent[yroot] = xroot
    rank[xroot] += rank[yroot]
    return True

edge_set = set()
for u, v in edges:
    if u > v:
        u, v = v, u
    edge_set.add((u, v))

result = []
for op in reversed(operations):
    if op[0] == 'cut':
        u, v = int(op[1]), int(op[2])
        if u > v:
            u, v = v, u
        edge_set.discard((u, v))
        union(u, v)
    else:
        u, v = int(op[1]), int(op[2])
        if find(u) == find(v):
            result.append("YES")
        else:
            result.append("NO")

for res in reversed(result):
    print(res)