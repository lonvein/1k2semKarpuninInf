q = []
ans = []
k = True
n, m = map(int, input().split())
l = [[] for _ in range(n + 1)]
lo = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    l[u].append(v)
    lo[v] += 1
for i in range(1, n + 1):
    if lo[i] == 0:
        q.append(i)
while q:
    if len(q) > 1:
        k = False  
    u = q.pop(0)
    ans.append(u)
    for v in l[u]:
        lo[v] -= 1
        if lo[v] == 0:
            q.append(v)  
if len(ans) != n:
    print(-1)
else:
    if k:
        print("YES")
    else:
        print('NO')
