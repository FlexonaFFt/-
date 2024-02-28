# def fib ():
#     n, k = map(int, input().split())
#     fib = [1, 1]
#     for _ in range(n-1):
#         fib.append(fib[-1] + fib[-2])
        
#         fib.pop(0)
        
#     print(fib[-1] % (10**k))

def last_k_digits_fibonacci(n, k):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    prev, curr = 1, 1
    for i in range(2, n + 1):
        prev, curr = curr, (prev + curr) % (10 ** k)
    
    return curr

# Ввод данных
n, k = map(int, input().split())

# Вывод результатов
print(last_k_digits_fibonacci(n, k))