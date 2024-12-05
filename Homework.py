import string
import keyword

input_string = input("Введіть рядок: ")

result = True

if input_string[0].isdigit():
    result = False
if any(c.isupper() for c in input_string):
    result = False
if any(c in string.punctuation and c != '_' for c in input_string) or any(c.isspace() for c in input_string):
    result = False
if input_string in keyword.kwlist:
    result = False
if input_string.count('_') > 1:
    result = False

print(result)