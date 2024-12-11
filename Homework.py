def common_elements():
    element_3 = {x for x in range(100) if x % 3 == 0}
    element_5 = {x for x in range(100) if x % 5 == 0}

    intersection = element_3 & element_5

    return intersection
result = common_elements()
print(result)