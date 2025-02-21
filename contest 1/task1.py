a, b = map(int, input().split())
def f(q, w):
    if q <= 1 or w <= 1:
        return 0
    if (q == 2 and w == 3) or (q == 3 and w == 2):
        return 1
    return f(q - 1, w-2) + f(q-2, w-1)
print(f(a, b))
