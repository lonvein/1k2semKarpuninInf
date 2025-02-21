n, m = map(int, input().split())
l = list(map(int, input().split()))
k = [0]*m
for i in l:
    k[k.index(min(k))] += i
print(max(k))