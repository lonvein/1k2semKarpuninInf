def f(l):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l = l[:i] + l[i+1] + l[i] + l[i+2:]
    return l
def g(l):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i][1] < l[i + 1][1]:
                d = l[i].copy()
                l[i] = l[i + 1]
                l[i + 1] = d
    return l


#l = list(map(str, input().split()))
l = ['eat', 'tea', 'ran', 'aet', 'ate', 'nra', 'bat']
ll = []
for i in range(len(l)):
    ll.append(f(l[i]))
for i in range(len(ll)):
    l[i] = [l[i], ll.count(ll[i])]
l = g(l)
for iii in range(len(l) - 1):
    for i in range(len(l) - 1):
        if (l[i][0] > l[i + 1][0]) and (l[i][1] == l[i + 1][1]):
            d = l[i].copy()
            l[i] = l[i + 1]
            l[i + 1] = d

t = ''
for i in range(len(l)):
    t = t + ' ' + str(l[i][0])
print(t[1:])