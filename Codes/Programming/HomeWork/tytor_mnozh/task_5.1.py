# Считываем все числа, подаваемые на input()
N, M = map(int, input().split())

# Заполняем множества номерами цветов кубиков Ани и Бори
colors_A = {int(n) for n in map(int, input().split(' '))}
colors_B = {int(n) for n in map(int, input().split(' '))}

# Находим пересечения множеств цвета, которые есть в обоих наборах
# А также находим цвета, находящиеся в одном множестве
general_colors = sorted(colors_A & colors_B)
filtered_colors_A = sorted(colors_A - colors_B)
filtered_colors_B = sorted(colors_B - colors_A)

# Выводим результат программы
print(len(general_colors), *general_colors)
print(len(filtered_colors_A), *filtered_colors_A)
print(len(filtered_colors_B), *filtered_colors_B)