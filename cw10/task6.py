a = int(input())
t = []
for i in range(a):
    s = list(map(int, input().split()))
    t.append(s)
xt = 0
for i in range(a):
    xt += t[i][0]
sx = xt/a
ac = 0
for i in range(a):
    if t.count([int(t[i][0]) + 2*(sx - int(t[i][0])), int(t[i][1])]):
        ac += 1
if ac == a:
    print('1')
else:
    print('0')