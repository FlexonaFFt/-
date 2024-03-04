first_ = input().split()
second_ = input().split()

print(*sorted(set(first_) & set(second_), key = int))