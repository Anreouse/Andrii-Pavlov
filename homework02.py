from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нулем.")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        """Скорочує дроби до їх найпростішого вигляду."""
        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

    def __mul__(self, other):
        """Виконує множення дробів."""
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        """Виконує додавання дробів."""
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Виконує віднімання дробів."""
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Перевіряє, чи дроби рівні."""
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        """Перевіряє, чи є цей дріб більшим за інший."""
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        """Перевіряє, чи є цей дріб меншим за інший."""
        return self.a * other.b < other.a * self.b

    def __str__(self):
        """Повертає рядкове представлення дробу."""
        return f"Fraction: {self.a}, {self.b}"

# Тестування
f_a = Fraction(2, 3)  # 2/3
f_b = Fraction(3, 6)  # 1/2 (скорочення)
f_c = f_b + f_a      # 1/2 + 2/3 = 7/6 (виміряється у чисельнику і знаменнику)
assert str(f_c) == 'Fraction: 7, 6'  # Виправлено

f_d = f_b * f_a      # 1/2 * 2/3 = 1/3
assert str(f_d) == 'Fraction: 1, 3'  # Виправлено

f_e = f_a - f_b      # 2/3 - 1/2 = 1/6
assert str(f_e) == 'Fraction: 1, 6'  # Виправлено

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)  # 1/2
f_2 = Fraction(3, 6)  # 1/2
assert f_1 == f_2  # True

print('OK')