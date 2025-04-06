def f1(lhn, n):
    f = [[] for i in range(n+1)]
    fe = []
    ans = 0 
    for vu in lhn:
        if dfs(f, vu[0], vu[1]) == 1:
            continue
        else:
            fe.append(vu)
            f[vu[0]].append(vu[1])
            f[vu[1]].append(vu[0])
            ans+=vu[2]
    return [ans, f]
def dfs(lhn, a, b, v = None, z = 0):
    if v is None and z == 0:
        v = set()
    if a not in v and z == 0:
        v.add(a)
        for nei in lhn[a]:
            if nei == b and z == 0:
                z += 1
            if z == 0:
                z = dfs(lhn, nei, b, v, z)
    return z
def bad(lhb, lp, p):
    clp = [0 for _ in range(p + 1)]
    for i in lhb:
        if (i[0] not in lp) and (i[1] in lp) and (i[2]>clp[i[1]]):
            clp[i[1]] = i[2]
        if (i[0] in lp) and (i[1] not in lp) and (i[2]>clp[i[0]]):
            clp[i[0]] = i[2]
    for i in lp:
        if clp[i] == 0:
            return 'bad'
    return sum(clp)
n, m, p = map(int, input().split())


lp = list(set(list(map(int, input().split()))))
p = len(lp)

lh = []
lhn = []
lhb = []
for i in range(m):
    neednow = list(map(int, input().split()))
    lh.append(neednow)
    if sum([1 if (neednow[0] == j or neednow[1] == j) else 0 for j in lp]) == 0:
        lhn.append(neednow)
    else:
        lhb.append(neednow)
lhn = sorted(lhn, key=lambda lhn: lhn[2])
lhb = sorted(lhb, key=lambda lhb: lhb[2])

a = bad(lhb, lp, n)
if a == 'bad':
    ANS = 'impossible'
else:
    ANS = bad(lhb, lp, n) + f1(lhn, n)[0]
for i in [ii + 1 for ii in range(n)]:
    if i not in lp:
        for j in [iii + 1 for iii in range(n)]:
            if j not in lp and dfs(f1(lhn, n)[1], i, j) == 0:
                ANS = 'impossible'
                break
    break
print(ANS)
