geniological_tree = dict()
n = int(input())

def solve(person, papa):
    if person == papa:
        return True
    while person in geniological_tree:
        person = geniological_tree[person]
        if person == papa:
            return True
    return False

for _ in range(n - 1):
    child, parent = input().split()
    geniological_tree[child] = parent

for _ in range(int(input())):
    first, second = input().split()
    if solve(second, first):
        print(1, end=" ")
    elif solve(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')