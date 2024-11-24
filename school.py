number = int(input("Введите число (5-значное): "))

#izvlekau chisla
a1 = number % 10
a2 = (number // 10) %10
a3 = (number // 100) %10
a4 = (number // 1000) %10
a5 = (number // 10000) %10

#perevarot chisel
number = a1 * 10000 + a2 * 1000+ a3 * 100 + a4 * 10 + a5

print(number)