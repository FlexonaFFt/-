cnt = int(input())
slovar = {}

# Алгоритм считывания строк и подсчёта количества слов
for _ in range(cnt):
    line = input().split()
    for word in line:
        if word not in slovar:
            slovar[word] = 0
        slovar[word] += 1

# Сортировка слов по убыванию частоты и лексикографическому порядку
sorted_words = sorted(slovar.items(), key=lambda x: (-x[1], x[0]))
for word, freq in sorted_words:
    print(word)