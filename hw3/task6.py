b = list(map(int, input().split()))
a = list(map(int, input().split()))
sua = 0
sub = 0
subb = 0
suab = 0
for i in range(len(a)):
    sua += a[i]
    sub += b[i]
    suab += (a[i]*b[i])
    subb += (b[i]*b[i])
sra = sua/len(a)
srb = sub/len(b)
srbb = subb/len(b)
srab = suab/len(a)
b = (srab - srb*sra)/(srbb - srb**2)
a = sra-b*srb
print(a, b)
