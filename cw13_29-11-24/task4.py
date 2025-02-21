def process_queries(n, arr, queries):
    from bisect import bisect_left, bisect_right
    results = []
    
    for i, j in queries:
        # Приводим индексы к нулевому основанию
        left = i - 1
        right = j - 1
        
        # Получаем подмассив
        subarray = arr[left:right + 1]
        
        # Инициализируем переменные для подсчета
        max_count = 0
        current_count = 1
        
        # Проходим по подмассиву и считаем максимальное количество
        for k in range(1, len(subarray)):
            if subarray[k] == subarray[k - 1]:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 1
        
        # Проверяем последний элемент
        max_count = max(max_count, current_count)
        
        results.append(max_count)
    
    return results

# Чтение входных данных
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    # Обработка запросов
    results = process_queries(n, arr, queries)
    
    # Вывод результатов
    for result in results:
        print(result)
        
