def fibonacci_modulo(n, k):
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, (a + b) % (10 ** (k + 1))
    return b

n, k = map(int, input().split())
result = fibonacci_modulo(n, k)
print(result)