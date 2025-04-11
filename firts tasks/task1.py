n = int(input('Введите число вершин '))
m = int(input('Введите число ребер '))
l = list()
for i in range(m):
    l.append(list(map(int, input().split())))
d = dict((item, []) for item in range(n))
for i in range(m):
    for j in range(2):
        d[l[i][j]].append(l[i][(j+1)%2])      
g = d


start = l[0][0]
visited = [False] * (n + 1)
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