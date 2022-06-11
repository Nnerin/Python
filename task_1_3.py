# Task 3.
# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля,
# и среднее арифметическое в противном случае.

import statistics

num1 = int(input("Add 1st number: "))
num2 = int(input("Add 2nd number: "))
num3 = int(input("Add 3d number: "))


if num1 != 0 and num2 != 0 and num3 != 0:
    print("\nСреднее геометрическое чисел: ", statistics.geometric_mean([num1, num2, num3]))
else:
    print("\nСреднее арифметическое чисел: ", statistics.mean([num1, num2, num3]))

