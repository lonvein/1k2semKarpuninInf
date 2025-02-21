aa = str(input())


def f(a):
    if len(a) < 4:
        return a
    else:
        b = 0
        for i in range(4):
            if ord(a[i]) < 91:
                b += 1
        if b >= 3:
            return a.upper()
        else:
            return a


print(f(aa))
