import math
a, b = map(int, input().split(' '))
print(f'Длина окружности равно {round(a * 2 * math.pi, 2)}. Площадь круга составляет {
      round(100 * (((a ** 2) * math.pi) / (b * b)), 2)} % от площади квадрата.')
