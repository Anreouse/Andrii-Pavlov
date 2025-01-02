def is_prime(n):
    """Перевіряє, чи є число простим."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(limit):
    """Генератор простих чисел до заданого ліміту."""
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

print(list(prime_generator(10)))