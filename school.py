def say_hi(name: str, age: int) -> str:
    if age <= 0:
        return "Возраст должен быть позитивным!!!."

    if age % 10 == 1 and age % 100 !=11:
        year_word = "год"
    elif 2 <= age % 10 <= 4 and not (12<= age %  100 <= 14):
        year_word = "года"
    else:
        year_word = "Лет"
    return f"Салют! Меня зовут {name}, мне {age} {year_word}."

print(say_hi("Мустафа", 20))
print(say_hi("Феофан", 21))