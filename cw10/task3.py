def w(l, c, s = 0):
    if len(l) == 0:
        return s
    for i in range(len(l)):
        if l[i] >= c:
            return w(l[(i + 1):], l[i], s + 1)
    else:
        return s 
l = list(map(int, input().split()))
t = ''
for i in range(len(l)):
    t = t + ' ' + str(w(l[(i+1):], l[i]))
t = t[1:-1] + '0'
print(t)