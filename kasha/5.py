def min_cost_climbing_stairs_optimized(cost):
    n = len(cost)
    if n == 0:
        return 0
    elif n == 1:
        return cost[0]
    
    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = current

    return min(prev1, prev2)

# Пример использования
cost = list(map(int, input().split()))
print(min_cost_climbing_stairs_optimized(cost))  # Вывод: 15
