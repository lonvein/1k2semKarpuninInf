def f(a, l):
    k=[0]*(a+1)
    k[0]=1
    for i in l:
        for j in range(a, i-1, -1):
            if k[j-i]:
                k[j]+=1
    if k[a]==3:
        return 1
    else:
        return 0
    
a = int(input())
l=list(map(int, input().split()))
p=[]
p.append(0)
k=int(sum(l)/3) 
print(f(a, l))
