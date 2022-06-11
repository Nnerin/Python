# Найти значение максимального элемента списка.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)

max = 0
for i in range(arrSize):
    if A[i]>max:
        max=A[i]

print("  ".join(map(str, A)))
print("=================")
print(f"Max number = {max}")