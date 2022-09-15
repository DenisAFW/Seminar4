# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


N = int(input())
list = []
for i in range(1,N+1):
    a = randint(-N,N+1)
    list.append(a)
print(list)

newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)
