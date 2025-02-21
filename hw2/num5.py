a=list(input().split())
print(    str( [ a[len(a)-1] if i==0 else  a[i-1] for i in range(len(a)) ] )    )