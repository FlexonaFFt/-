class_mates = [{'name': "Игорь", 'height': "193"},
               {'name': "Валентин", 'height': "194"},
               {'name': "Ярик", 'height': "188"},
               {'name': "Степан", 'height': "176"},
               {'name': "Рома", 'height': "183"},
               {'name': "Олег", 'height': "175"},
               {'name': "Данил Семенов", 'height': "175"},
               {'name': "Данила", 'height': "176"},
               {'name': "Данил Никольский", 'height': "175"}]

zadacha = int(input('Введите номер варианта [1, 2]: '))

if zadacha == 1:
    def sredniy_rost(class_mates):
        publick_height = 0
        for mate in class_mates:
            publick_height += int(mate['height'])
        sred = publick_height / len(class_mates)
        return sred

    answer = sredniy_rost(class_mates)
    print("Средний рост в группе: {:.2f} см".format(answer))

if zadacha == 2:
    class Group:
        def __init__(self, class_mates):
            self.class_mates = class_mates
            self._publick_height = 0
            self._sred = 0

        def sredniy_rost(self):
            for mate in self.class_mates:
                self._publick_height += int(mate['height'])
            self._sred = self._publick_height / len(self.class_mates)
            return self._sred

    group = Group(class_mates)
    answer = group.sredniy_rost()
    print("Средний рост в группе: {:.2f} см".format(answer))