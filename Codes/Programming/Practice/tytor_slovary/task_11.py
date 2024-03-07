geniological_tree = {}
heights = {}
n = int(input())

def height_counter(person):
    if person not in geniological_tree:
        return 0
    else:
        return 1 + height_counter(geniological_tree[person])

for i in range(n - 1):
    child, parent = input().split()
    geniological_tree[child] = parent

for person in set(geniological_tree.keys()).union(set(geniological_tree.values())):
    heights[person] = height_counter(person)

for key, value in sorted(heights.items()):
    print(key, value)