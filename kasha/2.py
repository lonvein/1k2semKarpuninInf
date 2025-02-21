def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Элемент найден
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине    
    return -1  # Элемент не найден
# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(f"Индекс элемента {target}: {result}") 
# Вывод: Индекс элемента 5: 4




