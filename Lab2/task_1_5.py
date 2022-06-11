# 1. Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
B = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))

for i in range(arrSize):
   if A[i] % 2 == 0:
      B.append(A[i])

if len(B) == 0:
   print("В массиве нет четных чисел")
   print(f"Первый элемент массива: {A[0]}")
else:
   minNum = min(B)
   print(f"Наименьшее четное число: {minNum}")

# 2. Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.
print("================================\n")

A = list(map(int,input('Введите числа через пробел\n').split()))
#print("  ".join(map(str, A)))
B = []
C = []
for i in range(len(A)):
   if A[i] == 0:
      B.append(A[i])
   else:
      C.append(A[i])
print("\nВывод:")
print(B + C)

