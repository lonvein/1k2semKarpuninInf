n = int(input())
j = []
def s(n, t):
    if n - 1 == 0:
        j.append(n)
        return t
    if (n % 3 == 0):
        t += 1
        j.append(n)
        return s(n / 3, t)
    if ((n - 1) % 3 == 0) and (n % 4 != 0) and ((((n - 1) / 3) % 3 == 0) or (((n - 1) / 3) % 2 == 0)):
        t += 1
        j.append(n)
        return s(n - 1, t)
    if (n % 2 == 0):
        t += 1
        j.append(n)
        return s(n / 2, t)
    if n - 1 != 0:
        t += 1
        j.append(n)
        return s(n - 1, t)
print(s(n, 0))