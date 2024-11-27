def add(x, y):                 #deg для определения функции  или задать функцию   # add функция для сложения  возврат функции
    return x + y                                          #  return  возврат функции

def subtract(x, y):             # subtract  функция для вычитания
    return x - y

def multiply(x, y):              # subtract  функция для умножения
    return x * y

def divide(x, y):            # divide  функция для деления
    if y == 0:                       #задаем функцию чтобы нельзя было делить на ноль
        return "деление на ноль нельзя, ошибка!"
    return x / y

def calculator():            # calculator  функция бесконечного цикла, пока человек не введет данные
    print("Выбирите вид операции кальулятора:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")  #функция ввода числа человеком

    num1 = float(input("Введите первое число: "))     # задаем функцию не целого первого числа
    num2 = float(input("Введите второе число: "))      # задаем функцию не целого второго числа

    if choice == '1':                                   # задаем функции каждого числа и результат операции
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Неверный ввод")                    #если введет номер операции выше >=5 или <=0
calculator()                            #замыкает функцию калькулятора