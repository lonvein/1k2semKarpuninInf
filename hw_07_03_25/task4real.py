a, b, c = map(int, input().split())
l = [[] for i in range(a + 1)]
for _ in range(b):
    x, y = map(int, input().split())
    l[x].append(y)
    l[y].append(x)


def ddfs(l, p1, p2): 
    visited = [None for _ in range(a + 1)]
    def dfs(i):   
        visited[i] = True
        for j in l[i]:
            if not(visited[j]):
                dfs(j)

    for i in l[p1]:
        if not(visited[i]):
            dfs(i)
    if visited[p2]:
        print('YES')
    else:
        print("NO")

for _ in range(c):
    act, p1, p2 = input().split()
    p1, p2 = int(p1), int(p2)
    if act == 'cut':
        l[p1].remove(p2)
        l[p2].remove(p1)
    else:
        ddfs(l, p1, p2)