def satisfied_children(n, greed_factors, m, cookie_sizes):
    greed_factors.sort()
    cookie_sizes.sort()
    
    children_satisfied = 0
    i = 0
    j = 0
    
    while i < n and j < m:
        if greed_factors[i] <= cookie_sizes[j]:
            children_satisfied += 1
            i += 1
        j += 1
    
    return children_satisfied

n = int(input())
greed_factors = list(map(int, input().split()))
m = int(input())
cookie_sizes = list(map(int, input().split()))
result = satisfied_children(n, greed_factors, m, cookie_sizes)
print(result)