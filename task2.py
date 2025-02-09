n = int(input('Введите число вершин '))
m = int(input('Введите число ребер '))
l = list()
for i in range(m):
    l.append(list(map(int, input().split())))
g = dict((item, []) for item in range(n))
for i in range(m):
    for j in range(2):
        g[l[i][j]].append(l[i][(j+1)%2])      


start = int(input('Введите начальную вершину '))
end = int(input('Введите конечную вершину '))
visited = [False] * (n + 1)
prev = [None] * (n + 1)
ans = 0
def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start 
            dfs(u, visited, prev, g)
dfs(start, visited, prev, g)
if visited[end] == True:
    print('Достяжимы')
else:
    print('Недостяжимы')