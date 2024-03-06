# Считывание первого числа
count = int(input("Введите количество цифр первого числа: "))
num_list = []
for _ in range(1, count + 1):
    num = int(input(f"Введите {_} цифру числа: "))
    num_list.append(num)

# Считывание второго числа 
num_2 = int(input("Введите второе число: "))

# Обработка списочной формы первого числа: 
num_1 = ''.join(str(e) for e in num_list)
int_num_1 = int(num_1)

# Сложение чисел и вывод ответа: 
rezult = int_num_1 + num_2
print(f"Результат: {rezult}")