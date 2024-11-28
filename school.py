
num1 = float(input("Введте первое число: "))

operator = input("Введите знак (+, -, *, /): ")

num2 = float(input("Введите второе число: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("На ноль делить нельзя.")
else:
    print("Ошибка")