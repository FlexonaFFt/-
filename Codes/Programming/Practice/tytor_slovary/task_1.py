"""string = str(input("Введите строку, которая подлежит обработке: "))

def UnicueWordCounter(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts

word_counts = UnicueWordCounter(string)
print(list(map(lambda x: str(word_counts[x]), word_counts))) """


text = input("Введите строку, которая подлежит обработке: ").split()
word_count = {}

for word in text:
    if word not in word_count:
        word_count[word] = 0
        print(0, end=' ')
    else:
        word_count[word] += 1
        print(word_count[word], end=' ')