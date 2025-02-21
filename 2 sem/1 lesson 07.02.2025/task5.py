h = [(0, 1, 3), (0, 4, 1), (1, 2, 1), (1, 3, 3), (1, 4, 1), (4, 2, 2), (4, 3, 1)]
g = {'0' : [['1', 3], ['4', 1]],
     '1' : [['2', 1], ['3', 3], ['4', 1]],
     '4' : [['2', 2], ['3', 1]]}
# где первые 2 цифры - ребро, а 3ья - вес
start = 0
end = 2
visited = [False, 10000] * (n + 1)
prev = [None] * (n + 1)
def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start 
            dfs(u, visited, prev, g)
dfs(start, visited, prev, g)
if visited.count(False) == 1:
    print('YES')
else:
    print('NO')