# Напишу функцию, которая будет искать делители и заносить их в список
"""
def factorization(num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            while num % i == 0:
                num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors"""

def factorization(num):
    d = 2
    while d * d <= num:
        if num % d == 0:
            print(d, end=' ')
            num //= d
        else:
            d += 1
    if num > 1:
        return num

input_nummer = int(input("Введите число: "))
print(factorization(input_nummer))