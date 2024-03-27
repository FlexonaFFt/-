'''
Подпоследовательностью данной строки (последовательности) 
называется некоторое подмножество символов исходной строк
и, следующих в том же порядке, в котором они идут в исход
ной строке, но не обязательно подряд.
'''

def podposledovatelnost(first_, second_):
    el_1, el_2 = 0, 0
    while el_1 < len(first_) and el_2 < len(second_):
        if first_[el_1] == second_[el_2]:
            el_1 += 1
        el_2 += 1
    return el_1 == len(first_)

first = str(input("Введите первую строку: "))
second = str(input("Введите вторую строку: "))
print(podposledovatelnost(first, second))