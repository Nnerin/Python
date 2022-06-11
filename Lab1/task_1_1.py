# Task 1.
# Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
'''
num1 = int(input("Add 1st number: "))
num2 = int(input("Add 2nd number: "))
num3 = int(input("Add 3d number: "))

count = 0

if num1 < 0:
    count += 1
if num2 < 0:
    count += 1
if num3 < 0:
    count += 1

print("QTY of negative numbers: ", count)
'''

# array + loop using
import random

arrSize = int(input("Введите кол-во чисел в массиве: "))
print("Add numbers")
count = 0
A = []
for _ in range(arrSize):
   a = int(input())
   A.append (a)
   if a < 0:
       count += 1

print("QTY of negative numbers: ", count)
