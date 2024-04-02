def calculate_hash(s, a, m):
    result = 0
    for char in s:
        result = (result * a + ord(char)) % m
    return result

a = int(input())
m = int(input())
s = input()
hash_value = calculate_hash(s, a, m)
print(hash_value)