# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import itertools
from random import randint


# k = int(input('Введите степень '))

# def random_numbers(k):
#     numbers = [randint(0,100) for i in range(k)]
#     while numbers[0] == 0:
#         numbers[0] = randint(1, 10) 
#     return numbers

# def urov(k, numbers):
#     f = ['*x^']*(k-1) + ['*x']
#     cheekibreeki = [[a, b, c] for a, b, c in itertools.zip_longest(numbers, f, range(k, 1, -1), fillvalue= '') if a != 0]
#     for x in cheekibreeki:
#         x.append(' + ')
#     cheekibreeki = list(itertools.chain(*cheekibreeki))
#     cheekibreeki[-1] = ' = 0'
#     return "".join(map(str, cheekibreeki)).replace(' 1*x', ' x')
# numbers = random_numbers(k)
# check_list = urov(k, numbers)
# print(check_list)

# with open('text.txt', 'w') as data:
#     data.write(check_list)

# #Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

# k = int(input('Введите степень второго многочлена '))

# numbers = random_numbers(k)
# check_list2 = urov(k,numbers)
# print(check_list2)

# with open('text2.txt', 'w') as data:
#     data.write(check_list2)

# Лучшее рещение
print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
k = int(input("Введите степень k: "))

factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('data.txt', 'w')
record.write(''.join(result))
record.close()
