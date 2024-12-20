from inspect import isgenerator
import types


def some_gen(start, n, func):
    """Генератор числової послідовності.

    Args:
        start: Перше значення прогресії.
        n: Кількість елементів, які генеруємо.
        func: Функція для обчислення наступного члена послідовності.
    """
    current = start
    for _ in range(n):
        yield current
        current = func(current, 2)  # Використовуємо функцію pow із заданою експонентою

gen = some_gen(2, 4, pow)

print(isinstance(gen,types.GeneratorType))
print(list(gen))