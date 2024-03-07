"""counter = {}

count = int(input("Введите количество строк в тексте: "))
for _ in range(1, count + 1):
    string = str(input(f"{_}: ").split())

for word in string:
    counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_popular = [k for k, v in counter.items() if v == max_count]
print(min(most_popular))"""

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))