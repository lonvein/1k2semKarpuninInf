def bfs(a, b):
    if a == b:
        return 0
    d = [float('inf') for i in range(10000)]
    d[a] = 0
    q = []
    q.insert(0, a)
    while q != []:
        u = q.pop()
        for v in [u-2, u*3, u + sum(map(int, str(u)))]:
            if v == b:
                return d[u] + 1
            if 1 <= v <= 9999 and d[v] == float('inf'):
                d[v] = d[u] + 1
                q.insert(0, v)
    return d[b]
a, b = map(int, input().split())
print(bfs(a, b))