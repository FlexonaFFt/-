class_mates = [{'name': "Игорь", 'height': "193"},
               {'name': "Валентин", 'height': "194"},
               {'name': "Ярик", 'height': "188"},
               {'name': "Степан", 'height': "176"},
               {'name': "Рома", 'height': "183"},
               {'name': "Олег", 'height': "175"},
               {'name': "Данил Семенов", 'height': "175"},
               {'name': "Данила", 'height': "176"},
               {'name': "Данил Никольский", 'height': "175"}]

def sredniy_rost(class_mates):
    publick_height = 0
    for mate in class_mates:
        publick_height += int(mate['height'])
    sred = publick_height / len(class_mates)
    return sred

answer = sredniy_rost(class_mates)
print("Средний рост в группе: {:.2f} см".format(answer))

# проверка
#print((193 + 194 + 188 + 176 + 183 + 175 + 175 + 176 + 175) / 9)