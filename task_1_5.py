# Task 5.
# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.


num1 = int(input("Add 1st number: "))
num2 = int(input("Add 2nd number: "))
num3 = int(input("Add 3d number: "))
num4 = int(input("Add 4th number: "))

if num1 % 2 != 0 or num2 % 2 != 0 or num3 % 2 != 0 or num4 % 2 != 0:
    print("\nЕсть нечетные числа")
else:
    print("\nВсе числа четные")

