"""def is_palindrome():
    string = input()
    for word in string.split():
        word = word.lower()
        word = ''.join(set(word))
    return word[::-1] == word

print(is_palindrome())"""

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

str = input("Введите строку: " + "\n")
print(is_palindrome(str))