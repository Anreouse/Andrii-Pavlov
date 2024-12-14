def find_unique_value(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    for number, count in frequency.items():
        if count == 1:
            return number

    return None
example_list_1 = [1, 2, 2, 3, 3]
example_list_2 = [4, 5, 4, 5, 7]
example_list_3 = [10, 10, 2, 3, 3]
example_list_4 = [6, 7, 8, 7, 6]

print(find_unique_value(example_list_1))
print(find_unique_value(example_list_2))
print(find_unique_value(example_list_3))
print(find_unique_value(example_list_4))