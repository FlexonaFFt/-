def find_longest_word(string):
    _words = list(map(str.strip, string.split())) # Разделяем текст на слова и удаляем пробелы
    longest_word = max(_words, key=len)
    return longest_word, len(longest_word)

Long = int(input("Введите длину текста: "))
String = str(input("Введите текст: "))

print(*find_longest_word(String))