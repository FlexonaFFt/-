'''def bubble_sortirovka(array):
    count = len(array)
    for i_num in range(count):
        swap = False
        for j_num in range(0, count - i_num - 1):
            if array[j_num] > array[i_num + 1]:
                array[j_num], array[j_num + 1] = array[j_num + 1], array[j_num]
                swap = True
        if not swap:
            break
        print(*array)'''

'''def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapp = True
        print(*a)

input_str = input("Введите числа через пробел: ")
arr = list(map(int, input_str.split()))
bubble_sort(arr)'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
        print(' '.join(map(str, arr)))

input_data = input("Введите длину массива и элементы через пробел: ")
n, *array = map(int, input_data.split())
bubble_sort(array)