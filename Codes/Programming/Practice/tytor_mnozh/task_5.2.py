# Считываем все числа, подаваемые на input()
# Заполняем множества номерами цветов кубиков Ани и Бори
A_cubes, B_cubes = map(int, input().split())
list_A = {input() for i in range(A_cubes)}
list_B = {input() for i in range(B_cubes)}

# Находим пересечения множеств цвета, которые есть в обоих наборах
# А также находим цвета, находящиеся в одном множестве
general_colors = list_A & list_B
filtered_colors_A = list_A - list_B
filtered_colors_B = list_B - list_A

# Выводим результат программы
print(len(general_colors))
print(' '.join(sorted(general_colors, key=int)))

print(len(filtered_colors_A))
print(' '.join(sorted(filtered_colors_A, key=int)))

print(len(filtered_colors_B))
print(' '.join(sorted(filtered_colors_B, key=int)))