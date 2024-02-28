def binary_addition(num1, num2):
    # Дополнение чисел нулями до равной длины
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = ''
    carry = 0
    
    # Сложение по разрядам
    for i in range(max_len-1, -1, -1):
        bit_sum = int(num1[i]) + int(num2[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
    
    if carry:
        result = '1' + result
    
    return result

# Ввод чисел в двоичной системе
num1 = input()
num2 = input()

# Вызов функции для сложения и вывод результата
print(binary_addition(num1, num2))


# def bin_sum():
#     number1 = int(input(), 2)
#     number2 = int(input(), 2)
#     sum = number1 + number2
#     print(bin(sum)[2:])

# bin_sum()