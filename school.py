my_list = [0,123,3,4,6,0,1,0,3,0,12,0,3,0,0,0,2,3,5]

result = []
zero_count = 0

for num in my_list:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1

result.extend([0] * zero_count)
print(result)