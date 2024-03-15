my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
max_key = max(my_dict, key=lambda k: ord(k))
print(f'Ключ с максимальным значением: {max_key}')