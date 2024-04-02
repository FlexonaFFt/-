from itertools import combinations

n = int(input())
s = int(input())
array = list(map(int, input().split()))

chetverki = set()

for comb in combinations(array, 4):
    if sum(comb) == s:
        chetverki.add(tuple(sorted(comb)))

chetverki = sorted(chetverki)

print(" ")
print(len(chetverki))
for quad in chetverki:
    print(*quad)