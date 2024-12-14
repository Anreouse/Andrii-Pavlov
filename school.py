def add_one(digits):
    number = int("".join([str(digit)for digit in digits]))
    number += 1
    result = [int(digit) for digit in str(number)]
    return result

user_input = input("Введіть цифри через пробіл: ")
digits = [int(digit) for digit in user_input.split()]
result = add_one(digits)
print("Результат:", result)