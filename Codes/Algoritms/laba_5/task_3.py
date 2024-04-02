counter = int(input())
string_list = []
for _ in range(1, counter + 1):
    string = str(input())
    string_list.append(string)

ans = []
for string in string_list:
    if string not in ans:
        ans.append(string)

print(' ')
for i in range(0, len(ans)):
    print(ans[i])