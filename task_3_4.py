# Найти значение минимального элемента списка.
import random

arrSize = int(input("Введите кол-во чисел в массиве: "))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)

min = 100
for i in range(arrSize):
    if A[i]<min:
        min=A[i]

print("  ".join(map(str, A)))
print("=================\n")
print(f"Min number = {min}")


