variant = int(input("Введите вариант решения задачи[1, 2]: "))

if variant == 1:
    def compare_characters(char1, char2):
        ord_char1 = ord(char1)
        ord_char2 = ord(char2)
        
        if ord_char1 > ord_char2:
            return f"{char1} ({ord_char1}) больше {char2} ({ord_char2})"
        elif ord_char1 < ord_char2:
            return f"{char1} ({ord_char1}) меньше {char2} ({ord_char2})"
        else:
            return f"{char1} ({ord_char1}) равен {char2} ({ord_char2})"

    # Пример использования
    symbol1 = 'h'
    symbol2 = 'р'
    result = compare_characters(symbol1, symbol2)
    print(result)

if variant == 2:
    dict = {
        "key7": 24,
        "key6": 9,
        "key71": 20,
        "key17": 17,
        "key201": 201
    }   

    max_dict_elem = max(dict.values())
    print("Максимальный элемент в словаре: ", max_dict_elem)
    max_val = max(dict.values())
    max_val_key = max(dict, key=dict.get)
    print("Максимальный элемент словаря: ", max_val, "и имеет ключ: ", max_val_key)
    print("Максимальный ключ словаря: ", max(dict))

    '''key=d.get применяет метод get() к каждому элементу словаря 
    для получения значений и находит ключ с максимальным значением.'''