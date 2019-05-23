import random

def AAaAaAAaaaA(s):
    charlist = list(s)
    new_chars = []
    for char in charlist:
        case_func = random.choice((str.upper, str.lower))
        new_chars.append(case_func(char))
    return ''.join(new_chars)

text = input('Voer tekst in: ')
print(AAaAaAAaaaA(text))
