def don(m, n):
    if n == 0:
        return (m, 1, 0)
    else:
        d, i, j = don(n, m % n)
        return d, j, i - j * (m // n)


a, b = map(int, input().split())
if max(a, b) == b:
    print(don(b, a)[::-1])
elif max(a, b) == a:
    print(don(a, b)[::-1][1], don(a, b)[::-1][0],  don(a, b)[::-1][2])
