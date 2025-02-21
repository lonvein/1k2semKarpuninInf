def w(l, c, s = 0):
    if len(l) == 0:
        return s
    for i in range(len(l)):
        if int(c) > int(l[i]):
            s += 1
    return s
def f(l):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if (l[i][1] > l[i + 1][1]):
                d = l[i].copy()
                l[i] = l[i + 1]
                l[i + 1] = d
    return l


tests = int(input())
asd = 1
ans = []
while asd <= tests:
    asd += 1
    letters, strings = input().split()
    li = []
    for i in range(int(strings)):
        l = input()
        l = l.replace('A', '1')
        l = l.replace('C', '2')
        l = l.replace('G', '3')
        l = l.replace('T', '4')
        li.append(l)
    for i in range(len(li)):
        ch = 0
        for h in range(len(li[i])):
            ch += w(li[i][h+1:], li[i][h])
        li[i] = [li[i], ch]
    ans.append(f(li))
for i in range(len(ans)):
    for g in range(len(ans[i])):
        ans[i][g][0] = ans[i][g][0].replace('1', 'A')
        ans[i][g][0] = ans[i][g][0].replace('2', 'C')
        ans[i][g][0] = ans[i][g][0].replace('3', 'G')
        ans[i][g][0] = ans[i][g][0].replace('4', 'T')
        print(ans[i][g][0])
    print('')