def w(l, c):
    if len(l) == 0:
        return -1
    for i in [len(l)-1-x for x in range(len(l))]:
        if l[i] >= c:
            return i
    else:
        return -1
l = list(map(str, input().split()))
t = ''
for i in range(len(l)):
    t = t + ' ' + str(w(l[0:i], l[i]))
print(t[1:])

