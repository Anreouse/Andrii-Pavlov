def difference(*args):
    if len(args) == 0:
        return 0
    max_value = max(args)
    min_value = min(args)
    diff = max_value - min_value
    return round(diff, 2)
print(difference(5,-5))