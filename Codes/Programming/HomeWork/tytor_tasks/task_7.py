count = int(input())
all_nums = set(range(1, count+1))
def_nums = all_nums
while True:
    guess = input()
    if guess == "HELP":
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        def_nums &= guess
    else:
        def_nums &= all_nums - guess

print(" ".join([str(x) for x in sorted(def_nums)]))