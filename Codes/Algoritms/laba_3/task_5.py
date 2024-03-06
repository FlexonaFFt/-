# # Прописываю функцию сортировки вещей
# def sort_clothes(n, colors):
#     result = [0] * n
#     i, j, k = 0, 0, 0
#     for color in colors:
#         if color == 0:
#             result[i] = color 
#             i += 1
#         elif color == 1:
#             result[j] = color 
#             j += 1
#         elif color == 1:
#             result[k] = color 
#             k += 1
#     return result

# num = int(input("Введите количество элементов одежды: "))
# colors = list(map(int, input().split()))
# sorted_clothes = sort_clothes(num, colors)
# print(*sorted_clothes)

# Считываем количество предметов в гардеробе
n = int(input())

# Считываем массив цветов для каждого предмета
colors = list(map(int, input().split()))

# Создаем три пустых списков для каждого цвета
pink = []
yellow = []
raspberry = []

# Проходим по массиву цветов и добавляем предметы в соответствующие списки
for color in colors:
    if color == 0:
        pink.append(color)
    elif color == 1:
        yellow.append(color)
    elif color == 2:
        raspberry.append(color)

# Объединяем списки в правильном порядке
sorted_colors = pink + yellow + raspberry

# Выводим цвета предметов в правильном порядке через пробел
print(' '.join(map(str, sorted_colors)))
