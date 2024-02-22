numbers = input()
numbers_list = list(map(int, numbers.split()))
result = len(set(numbers_list))
print(result)