seconds = int(input("Введіть кількість секунд (0 < seconds < 8640000): "))

if 0 <= seconds < 8640000:

    days, remainder = divmod(seconds, 86400)  # 86400 сек в дні
    hours, remainder = divmod(remainder, 3600)  # 3600 сек в годинах
    minutes, seconds = divmod(remainder, 60)  # 60 сек в хвилинах

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    print( f"Час у вигляді: {days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print("Введене число повинно бути в межах від 0 до 8640000.")