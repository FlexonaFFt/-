def game_checker(a, b, c):
    if (a % 2 == b % 2) and (b % 2 == c % 2):
        return "WIN"
    else:
        return "FAIl"

print("Введите три случайных значения: ")
first_, second_, third_ = map(int, input("Значения: ").split())
print(game_checker(first_, second_, third_))