li = list(map(int, input().split(' ')))
# print(int(str([i for i in range(1, l[0]+1) if l[1::].count(i)==0])[1:-1]))
for i in range(1, li[0]+1):
    if li[1::].count(i) == 0:
        print(i)
