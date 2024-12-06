seconds = int(input("Введіть кількість секунд (0 < seconds < 8640000): "))

if 0 <= seconds < 8640000:

    days, remainder = divmod(seconds, 86400)  # 86400 сек в дні
    hours, remainder = divmod(remainder, 3600)  # 3600 сек в годинах
    minutes, seconds = divmod(remainder, 60)  # 60 сек в хвилинах

    day_word = "день" if days == 1 else "дні" if 1 < days < 5 else "днів"
    print(
        f"Час у вигляді: {days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print("Введене число повинно бути в межах від 0 до 8640000.")