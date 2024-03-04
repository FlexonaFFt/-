inp = int(input("Введите количество синонимов: "))
spisok = {}
for i in range(inp):
    first_, second_ = input().split()
    spisok[first_] = second_
    spisok[second_] = first_
print(spisok[input("Введите слово для поиска: ")])