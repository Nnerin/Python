# Удалить из списка все элементы, совпадающие с его минимальным значением.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(1, 5)
   A.append(a)

min = 100
for i in range(arrSize):
    if A[i]<min:
        min=A[i]

print(str(A).strip('[]'))
print("=================\n")
print(f"Min number = {min}")

for i in range(arrSize):
   if min in A:
      A.remove(min)
print(str(A).strip('[]'))