def generate_cube_numbers(limit):
    number = 2
    while True:
        cube = number ** 3
        if cube > limit:  # виправлено для включення граничного значення
            return
        yield cube
        number += 1

# Приклад використання генератора:
for cube in generate_cube_numbers(1000):
    print(cube)