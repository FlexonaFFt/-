numbers = input().split()
used_numbers = set()

for number in numbers:
    if number in used_numbers:
        print("YES")
    else:
        print("NO")
        used_numbers.add(number)