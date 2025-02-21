while True:
    n, k = map(int, (input().split()))
    l = list(map(int, input().split()))
    if n == k:
        print(str(sorted(l)).replace(',', '')[1:-1])
        break
    t = l[0:k]
    for i in range(k, len(l)):
        if l[i] < t[-1]:
            t[-1] = l[i]
            t = sorted(t)
    print(str(t).replace(',', '')[1:-1])
    break
        
        
        
