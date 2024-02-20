number = input('Введите число: ')

max_digit = max(number)
min_digit = min(number)

index_max = number[::-1].index(max_digit) + 1
index_min = number[::-1].index(min_digit) + 1
index_max_start = number.index(max_digit) + 1
index_min_start = number.index(min_digit) + 1


print(index_max_start, index_max)
print(index_min_start, index_min)

