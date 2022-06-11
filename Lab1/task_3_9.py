# Найти среднее арифметическое элементов списка.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))

sum = 0
for i in range(arrSize):
   sum += A[i]

arrLen = len(A)
mean = sum/arrLen
print(f"Mean = {mean}")

