a = int(input())
l=[]
b=[]
l.append(1)
def f(q, w, k, l=[]):
    if w==q:
        return k, l
    if w*3>q:
        if w*2>q:
            return f(q, w+1, k+1, l+[1])  
        else:
            return f(q, w*2, k+1, l+[2])
    else:
        return min(f(q, w*3, k+1, l+[3]), f(q, w*2, k+1, l+[2]), f(q, w+1, k+1, l+[1]))

d=f(a, 1, 0, l)
vv=d[0]
v=d[1][1:]
for i in range(len(v)-1, -1, -1):
    if v[i]==3 and v[i-1]==2:
        t = v[i]
        v[i] = v[i-1]
        v[i-1] = t
        t = 0
h='1'
hh=1
for i in v:
    if i==1:
        hh+=1
        h=h+' '+str(hh)
    if i==2:
        hh*=2
        h=h+' '+str(hh)
    if i==3:
        hh*=3
        h=h+' '+str(hh)
print(vv)
print(h)
