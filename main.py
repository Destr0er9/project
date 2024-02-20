number = input('Введите число: ')
first_number = number[0]
count = 0

for i in range(len(number)):
    if first_number in number[i]:
        count += 1

print(count)
