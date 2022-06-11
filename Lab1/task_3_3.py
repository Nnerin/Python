# Task 3.
# Удалить элементы, индексы которых кратны 7.
import random

arrSize = int(input("Введите кол-во чисел в массиве: "))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)

print("  ".join(map(str, A)))
print("=================\n")

if arrSize > 7:
    del A[7::7]
    arrSize = len(A)
    print("  ".join(map(str, A)))
else:
    print("Array size < 8\n")
