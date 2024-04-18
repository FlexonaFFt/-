import sys
from collections import defaultdict

n = int(sys.stdin.readline())

graph = defaultdict(list)

for i in range(1, n):
    line = sys.stdin.readline().strip()
    for j in range(n - i):
        if line[j] == 'B':
            graph[i].append(i + j + 1)
            graph[i + j + 1].append(i)
        elif line[j] == 'R':
            graph[i].append(i + j + 1)

def check(start=1):
    colors = [0] * (n + 1)
    this_color = 1
    ans = True

    for k in range(1, n + 1):
        stack = [(k, this_color)]
        while stack:
            v = stack.pop()
            u = v[0]
            color = v[1]

            if colors[u] == 0:
                colors[u] = color

                for uu in graph[u]:
                    if colors[uu] == color:
                        ans = False
                    if colors[uu] == 0:
                        stack.append((uu, 3 - color))

    if ans:
        print("YES")
    else:
        print("NO")

check()