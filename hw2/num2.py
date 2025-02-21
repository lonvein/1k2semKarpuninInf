l=list(map(str, input().split(' ')))
a=int(l[0])
b=str(l[1])
c=int(len(b)/a)
ss=[]

for i in range(a):
    ss= ss + list(l[1][c*i : c*(i+1)])[::-1]
n=str()
for i in range(len(b)):
    n = n + str(ss[i])
print(n)