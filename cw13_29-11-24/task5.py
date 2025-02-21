t = int(input())

while t>0:
    ans = []
    t -= 1
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    s = set(l)
    ls = len(s)
    x = [[l[i], [l[:i+1].count(j) for j in s]]for i in range(len(l))]
    for i in range(q):
        an = []
        a, b = map(int, input().split())
        if a == b:
            ans.append(1)
        elif a - 2 == -1:
            ans.append(max(x[b-1][1]))
        else:
            xx = []
            for k in range(ls):
                xx.append(x[b-1][1][k] - x[a-2][1][k]) 
            ans.append(max(xx))
    print(str(ans)[1:-1].replace(', ', '\n'))

