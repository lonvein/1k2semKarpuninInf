n = int(input('Введите число пунктов назначения '))
m = int(input('Введите число рейсов '))
g = list()
ll = list()
for i in range(m):
    lm = list(map(str, input().split()))
    g.append(lm)
    ll.append(lm[0])
    ll.append(lm[1])
for i in set(ll):
    if ll.count(i) == 1 and ll.index(i) % 2 != 0:
        g.append([i, 'NONE'])
ans = []
to = "NONE"
n = 4
b = 0

for ii in range(n):
    if g == []:
        print(ans)
        break
    for i in range(n - b):
        if g[i][1] == to:
            to = g[i][0]
            if len(g) == 1:
                ans.append(to)
                break
            else: 
                ans.append(to)
            g.pop(i)
            b += 1
            break
                
print(str(ans[::-1]).replace(', ', ' --> ').replace('[', '').replace(']', ''))