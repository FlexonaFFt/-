class_9 = []
class_10 = []
class_11 = []

for _ in range(5):
    input_data = input("Введите номер класса и фамилию ученика: ")
    class_number, name = input_data.split()
    if class_number == '9':
        class_9.append((name, '9'))
    elif class_number == '10':
        class_10.append((name, '10'))
    elif class_number == '11':
        class_11.append((name, '11'))
    else:
        print("Неверный номер класса. Введите '9', '10' или '11'.")
        continue

for class_list in [class_9, class_10, class_11]:
    class_list.sort()
    for name, class_number in class_list:
        print(f"{class_number} {name} ")
