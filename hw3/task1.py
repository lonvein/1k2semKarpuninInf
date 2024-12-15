a = int(input())
cache = [0 for i in range(1000)]


def f(n, cache):
    if n == 0:
        cache[n] = 0
        return cache[n]
    if n == 1:
        cache[n] = 1
        return cache[n]
    if cache[n] != 0:
        return cache[n]
    x = f(n-1, cache) + f(n-2, cache)
    cache[n] = x
    return x


print(f(a, cache))
