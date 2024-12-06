import string

input_str = input("Введіть два символи через дефіс: ")

start_index, end_index = [string.ascii_letters.index(c) for c in input_str.split('-')]

result = string.ascii_letters[start_index:end_index + 1]

print("Результат:", result)