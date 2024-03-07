commands = { 'read': 'R', 'write': 'W', 'execute': 'X' }
file_permisions = {}

# Алгоритм присваивания имени файлу и допустимых команд
for _ in range(int(input())):
    file_name, *permisions = input().split()
    file_permisions[file_name] = set(permisions)

# Алгортим проверки 
for _ in range(int(input())):
    move, file = input().split()
    if commands[move] in file_permisions[file]:
        print("OK")
    else:
        print("Access denied")
