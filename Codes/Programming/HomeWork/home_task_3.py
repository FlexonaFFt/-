'''
def proverka_word_is_palindrome(word):
    # Приводим слово к нижнему регистру и удаляем пробелы
    word = word.lower().replace(" ", "")
    # Сравниваем слово с перевернутой версией
    return word == word[::-1]

def proverka_palindrome_in_string(text):
    # Разбиваем строку на слова
    words = text.split()
    # Проверяем каждое слово на палиндром
    words = words.replace(".", "").replace(",", "")
    palindromes = [word for word in words if word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1]]
    return palindromes

def proverka_1(func, word):
    if func(word):
        print(f"{word} - это палиндром")
    else:
        print(f"{word} - не является палиндромом")

def proverka_2(func, string):
    if func(string):
        print(f"В строке '{string}' найдены следующие палиндромы: {', '.join(func)}")
    else:
        print(f"В строке '{string}' нет палиндромов")

primer = int(input("Решение через слово, строку --> [1, 2]:"))

if primer == 1:
    input_word = str(input("Введите слово: "))
    proverka_1(proverka_word_is_palindrome, input_word)

if primer == 2:
    input_string = str(input("Введите строку: "))
    proverka_2(proverka_word_is_palindrome, input_string)'''

def proverka_word_is_palindrome(word):
    # Приводим слово к нижнему регистру и удаляем пробелы
    word = word.lower().replace(" ", "")
    # Сравниваем слово с перевернутой версией
    return word == word[::-1]

def proverka_1(func, word):
    if func(word):
        print(f"{word} - это палиндром")
    else:
        print(f"{word} - не является палиндромом")

input_word = str(input("Введите слово: "))
proverka_1(proverka_word_is_palindrome, input_word)