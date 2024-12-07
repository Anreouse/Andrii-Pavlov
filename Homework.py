user_input = int(input("Enter a number: "))

while user_input >9:
    product = 1
    n = user_input

    while n > 0:
        product *= n % 10
        n = n//10

    user_input = product

print("Result:", user_input)