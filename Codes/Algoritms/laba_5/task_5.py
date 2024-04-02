def opa_nifiga(s, t):
    if len(s) != len(t):
        return "NO"

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return "NO"
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return "NO"
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s
    return "YES"

first = input()
second = input()
result = opa_nifiga(first, second)
print(result)
