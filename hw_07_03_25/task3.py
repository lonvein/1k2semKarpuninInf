'''4 5 
3 4 8 >= 
2 3 5 >= 
1 2 7 >= 
1 4 3 <= 
1 4 9 <='''

n, m = map(int, input().split())
l = [[-float('inf') for i in range(m+1)] for ii in range(m)]
print(l)
for _ in range(m):
    a, b, c, d = input().split()
    print(d)
    if d == '<=':
        l[int(a)][int(b)] = min(int(c), l[int(a)][int(b)])
    else:
        l[int(a)][int(b)] = max(-int(c), l[int(a)][int(b)])
print(n, m, l)



