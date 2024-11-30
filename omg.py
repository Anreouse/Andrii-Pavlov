import random

length = random.randint(3, 10)

# Створюємо список випадкових чисел в діапазоні від 1 до 100
original_list = [random.randint(1, 100) for i in range(length)]

# Создаю список з 3 елементів
new_list = [
    original_list[0],             # Перший елемент
    original_list[2],             # Третій елемент
    original_list[-2]             # Другий з кінця
]

print(original_list)
print(new_list)