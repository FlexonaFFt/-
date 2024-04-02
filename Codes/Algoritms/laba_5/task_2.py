'''def find_longest_unique_substring(s):
    count = {}
    max_len = 0
    start = 0
    for i, c in enumerate(s):
        if c in count:
            if i - start > max_len:
                max_len = i - start
                count[c] = i
            continue
        count[c] = i
    return max_len

s = str(input())
print(find_longest_unique_substring(s))'''

def longest_substring(s):
    start = 0
    max_length = 0
    used_chars = {}

    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used_chars[char] = i
    return max_length

input_string = str(input())
result = longest_substring(input_string)
print(result)

