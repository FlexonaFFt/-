def transpose_mat(mat):
    return list(map(list, zip(*mat)))

print('Введите размер матрицы: ')
n = int(input())
m = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
# считывает каждую строку матрицы, разделяет элементы по пробелам, 
# преобразует их в целые числа и сохраняет в виде списка списков.

transpose_matrix = transpose_mat(matrix)

for i in transpose_matrix:
    print(" ".join(map(str, i)))