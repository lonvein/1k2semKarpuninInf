n = int(input('Введите число вершин '))
m = int(input('Введите число ребер '))
l = list()
for i in range(m):
    l.append(list(map(int, input().split())))
d = dict((item, []) for item in range(n))
for i in range(m):
    for j in range(2):
        d[l[i][j]].append(l[i][(j+1)%2])      
graph = d

color = ['white' for i in graph.keys()]
prev = [None] * (n + 1)

def dfs(graph, v, color, prev):  
    color[v] = 'gray'
    for u in graph[v]:
        if color[u] == 'white':
            prev[v] = u
            dfs(graph, u, color, prev)
        elif color[u] == 'gray' and prev[u] != v:
            return True

if dfs (graph, 0, color, prev):
    print("Циклично")

else:
    print("Не циклично")

