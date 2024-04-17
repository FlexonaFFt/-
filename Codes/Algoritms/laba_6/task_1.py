n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

for vertex in graph:
    graph[vertex].sort()
print()
for vertex in graph:
    print(len(graph[vertex]), *graph[vertex])

'''
В этом решении мы сначала создаем список смежности 
как словарь, где ключом является номер вершины, 
а значением - список смежных вершин.
'''