def calculator():

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
                return
        else:
            print("Error operator")
            return

        print(f"Результат: {result}")

if __name__ == "__main__":
    calculator()