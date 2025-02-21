a = list(map(int, input().split()))
s='*'
for i in a:
    s=s+str(i)+'*'
l=0
for i in range(max(a)):
    g=0
    if s.find('*'+str(i)+'*')>0:
        l+=1
        g=i
        if l==len(a)//2 +1:
            print(g)
            break
        

        
