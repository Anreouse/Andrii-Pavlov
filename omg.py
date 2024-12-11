def second_index(search_string, text):
    first_index = text.find(search_string)
    if first_index == -1:
        return None

    second_index = text.find(search_string, first_index + len(search_string))
    return second_index if second_index != -1 else None

print(second_index("o", "i love you"))
print(second_index("e", "happy new year"))
