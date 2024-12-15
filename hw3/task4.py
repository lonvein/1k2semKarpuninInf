a, b = map(str, input().split())
if int(a) % 2 == 0:
    print('Вот ваш усеченный треугольник')
    for i in range(int(a) // 2 + 1):
        print(b * i)
    for i in range(int(a) // 2, 0, -1):
        print(b * i)
else:
    print('Вот ваш нормальный треугольник')
    for i in range(1, int(a) // 2 + 2):
        print(b * i)
    for i in range(int(a) // 2, 0, -1):
        print(b * i)
