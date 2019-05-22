import random

def AAaAaAAaaaA(s):
    charlist = list(s)
    new_chars = []
    for char in charlist:
        if random.choice((True, False)):
            new_chars.append(char.upper())
        else:
            new_chars.append(char.lower())
    return ''.join(new_chars)

text = input('Voer tekst in: ')
print(AAaAaAAaaaA(text))
