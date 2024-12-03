while True:
    operation = input("Введіть операцію (+, -, *, /) або 'exit' для виходу: ")

    if operation.lower() == 'exit':
        print("Вихід з калькулятора.")
        break

    num1_str = input("Введіть перше число: ")
    num2_str = input("Введіть друге число: ")

    num1 = float(num1_str)
    num2 = float(num2_str)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ділення на нуль неможливе.")
            continue
    else:
        print("Невідома операція.")
        continue

    print(f"Результат: {result}")

    continue_cal = input("Хочете виконати ще одне обчислення? (так/y/ні/n): ").strip().lower()
    if continue_cal not in ['так', 'y', 'yes']:
        print("Дякую, що скористалися калькулятором!")
        break