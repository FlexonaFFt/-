'''phone_numbers = {'2' : 'abc', '3': 'def', '4': 'ghi',
                 '5': 'jkl', '6': 'mno', '7': 'pqrs',
                 '8': 'tuv', '9': 'wxyz'}

def combinator(numbers):
    data = []
    symb = phone_numbers[numbers[-1]]
    for combination in combinator(numbers[:-1:]):
        for c in symb:
            data.append(combination + c)
    return data

print(' '.join(combinator(input())))'''

def combinations(input_string):
    d = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}

    # Это условие обязательно для выполнения кода
    if input_string == '':
        return ['']

    data = []
    word = d[input_string[-1]]
    for combination in combinations(input_string[:-1:]):
        for c in word:
            data.append(combination + c)
    return data


print(' '.join(combinations(input())))
