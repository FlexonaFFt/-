latin_to_english = {}
num_ = int(input())
for _ in range(num_):
    english_word, latin_translation_block = input().split(" - ")
    latins_translations = latin_translation_block.split(", ")
    for latin_word in latins_translations:
        if latin_word in latin_to_english:
            latin_to_english[latin_word].append(english_word)
        else:
            latin_to_english[latin_word] = [english_word]

print(len(latin_to_english))
for latin_word in sorted(latin_to_english.keys()):
    english_translations = latin_to_english[latin_word]
    print(latin_word + ' - ' + ', '.join(english_translations))