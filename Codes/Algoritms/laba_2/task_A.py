def formula(a, x, b, c):
    return a * x ** 2 + b * x + c 

print("Введите значения функции через пробел (a, x, b, c): ")
a_, x_, b_, c_ = map(int, input("Значения: ").split())
print(formula(a_, x_, b_, c_))