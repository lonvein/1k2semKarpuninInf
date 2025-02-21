from collections import Counter

t = int(input())

while t > 0:
    t -= 1
    ans = []
    n, q = map(int, input().split())
    l = list(map(int, input().split()))

    for _ in range(q):
        a, b = map(int, input().split())
        # Получаем подмассив от a-1 до b (включительно)
        sub_array = l[a-1:b]
        
        # Подсчитываем частоту элементов в подмассиве
        freq = Counter(sub_array)
        
        # Находим элемент с максимальной частотой
        max_freq = max(freq.values())
        
        ans.append(max_freq)

    print("\n".join(map(str, ans)))