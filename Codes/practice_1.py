# Вариант 4
# Задание 1 
import math
func = int(input("Выберите задание для решения: "))

if func == 1:
    def functuion1(a, b, c, d, f):
        if a == 0:
            return "No, a / 0 - nelza"
        else:
            formula = abs(a - b * c * d**3) + (c**5 - a**2) / a + f**3 * (a - 213)
            return formula

    print("Введите числа для подсчёта формулы функции: ")
    num_a = int(input("Число a:"))
    num_b = int(input("Число b:"))
    num_c = int(input("Число c:"))
    num_d = int(input("Число d:"))
    num_f = int(input("Число f:"))
    print(functuion1(num_a, num_b, num_c, num_d, num_f))

# Задание 2
if func == 2:
    spisok = [1, 23, 16, "25", "кефир", 8, 21]
    otvet = []
    for el in spisok:
        try:
            if int(el) % 2 != 0:
                otvet.append(int(el))
        except:
            pass


# Задание 3
if func == 3:
    spisok = [1, 23, 16, 135, 16, 8, 21, 34, 35]
    result = 1
    for number in spisok:
        if number < 10:
            result *= number
    print(result)

# Задание 4
if func == 4:
    spisok = [1, 23, 16, 135, 16, 8, 21, 34, 35]
    if len(spisok) % 2 == 0:
        print("Список содержит четное количество элементов")
    else:
        middle_number = spisok[len(spisok) // 2]
        print(f"Число, находящееся посередине массива: {middle_number}")