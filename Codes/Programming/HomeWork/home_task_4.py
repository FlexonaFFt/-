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