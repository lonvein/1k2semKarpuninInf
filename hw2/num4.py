a=list(input().split())
print(    str( [ a[i+(-1)**i] if len(a)%2==0 else (a[i+(-1)**i] if i<(len(a)-1) else a[len(a)-1])  for i in range(len(a))] )    )