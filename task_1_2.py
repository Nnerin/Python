# Task 2.
# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

num1 = int(input("Add 1st number: "))
num2 = int(input("Add 2nd number: "))
num3 = int(input("Add 3d number: "))

count = False

if num1 == num2 or num1 == num3 or num2 == num3:
    count = True

if count:
    print("\nThere are identical numbers")
else:
    print("\nThere are no identical numbers")

