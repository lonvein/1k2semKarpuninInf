# Проверка графа на двудольность с помощью теоремы Кенига

G = []
k = -1
for i in open("input1.txt", "r"):
    k += 1
    if k >= 1:
        G.append(list(map(int, i[:-1].split())))
n = len(G)
gg = [[] for _ in range(n+1)]
for i in G:
    print(i)
    gg[i[0]].append(i[1])
    gg[i[1]].append(i[0])
G = gg
print(G)
n = len(G)



def dfs(start, visited, g, ok):
    if visited[start] == 0:
        visited[start] = 1
    for u in g[start]:
        ok.append(visited[u]==visited[start])
        if visited[u] == 0:
            if visited[start] == 1:
                visited[u] = 2
            elif visited[start] == 2:
                visited[u] = 1
            dfs(u, visited, g, ok)

    return ok


visited = [0] * n
ok = dfs(1, visited, G, [])

output1 = open('output1.txt', 'w')
if max(ok):
    output1.write('YES')
else:
    output1.write('NO')
output1.close()