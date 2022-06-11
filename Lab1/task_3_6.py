# Удалить все элементы с заданным значением, если они имеются в списке.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 10)
   A.append(a)

print(str(A).strip('[]'))
print("========================")

delNumber = int(input("Введите число: \n"))
for i in range(arrSize):
   if delNumber in A:
      A.remove(delNumber)
print(str(A).strip('[]'))