import string


def is_palindrome(s):
    cleaned_s = ""

    for character in s:
        if character.isalnum():
            cleaned_s += character.lower()
    return cleaned_s == cleaned_s[::-1]


# Приклад використання функції
test_strings = [
    "Madam, in Eden, I'm Adam",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon",
    "Not a palindrome",
    "123145",
    "123321"
]
for test in test_strings:
    result = is_palindrome(test)
    print(f'"{test}" -> {result}')