# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input())

list = []

for i in range(1,N+1):
    if N % i == 0:
        list.append(i)
print(list)