import re

def first_word(text):
    match = re.match(r"[\W_]*([a-zA-Zа-яА-Я'\-]+)", text)
    if match:
        return match.group(1)
    return ''

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))