def is_correct_bracket_seq(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        elif bracket in brackets.keys():
            if not stack or brackets[bracket] != stack.pop():
                return False

    return not stack

# Использования функции
bracket_sequence = input()
result = is_correct_bracket_seq(bracket_sequence)
print(result)