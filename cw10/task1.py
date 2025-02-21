def w(c, p = 0):
    for i in range(len(c)):
        p += int(c[i])
    if p >= 10:
        return w(str(p))
    else:
        return p
def f(l):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if (l[i][0] > l[i + 1][0]) or ((l[i][0] == l[i + 1][0]) and (l[i][1] > l[i + 1][1])):
                d = l[i].copy()
                l[i] = l[i + 1]
                l[i + 1] = d
    return l
l = list(map(str, input().split()))
ll = []
for i in range(len(l)):
    ll.append([w(l[i]), int(l[i])])
ans = ''
lll = f(ll)
for i in lll:
    ans = ans + ' ' + str(i[1])
print(ans[1:])
