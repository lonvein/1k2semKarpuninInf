def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Список, где True означает "простое"
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

# Пример использования
n = int(input())
print(f"Простые числа до {n}: {sieve_of_eratosthenes(n)}")
