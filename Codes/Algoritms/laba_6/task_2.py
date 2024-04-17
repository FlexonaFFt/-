capacity = int(input())
heaps_count = int(input())
gold_heaps = []

for i in range(heaps_count):
    c, m = map(int, input().split())
    gold_heaps.append((c, m))

gold_heaps.sort(key=lambda x: x[0], reverse=True)
max_cost = 0

for i in gold_heaps:
    if capacity == 0:
        break
    if capacity >= i[1]:
        max_cost += i[0] * i[1]
        capacity -= i[1]
    else:
        max_cost += i[0] * capacity
        capacity = 0

print(max_cost)

'''
После того, как все кучи золота будут прочитаны, 
список gold_heaps сортируется в порядке убывания 
на основе стоимости за единицу веса каждой кучи золота. 
'''