n, m = map(int, input().split())
l = [[] for _ in range(n+1)]
for i in range(m):
    q, w = map(int, input().split())
    l[q].append(w)

print(l)


def ts(n, l, ans):
    ans = []
    visited = [False for _ in range(n+1)]
    for v in [i + 1 for i in range(n)]:
        if not visited[v]:
            dfs(l, v, visited, ans)
    ans.reverse()


def dfs(l, u, visited, ans):
    visited[u] = True
    for v in l[u]:
        if not visited[v]:
            dfs(v)
    ans.append(u)