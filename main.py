a = int(input('Введите число: '))

max_digit = max(str(a))
min_digit = min(str(a))

print(f'Максимальное число: {max_digit}, Минимальное число: {min_digit}')
print(f'Разница в числах: {int(max_digit) - int(min_digit)}')
print(f'Сумма чисел: {int(max_digit) + int(min_digit)}')

