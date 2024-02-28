def extra_chars(s, t):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return char
        
    for key, value in count.items():
        if value != 0:
            return key
    
s = input('Введите первую строку символов: ')
t = input('Введите вторую строку символов: ')
print(extra_chars(s, t))