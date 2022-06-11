# Найти среднее арифметическое трех последних элементов списка.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))

A.reverse()
#print("  ".join(map(str, A)))

if len(A)<3:
   print("Кол-во элементов массива меньше 3!")
else:
   sum = 0
   for i in range(3):
      sum += A[i]
   mean = 0
   mean = sum/3
   print(f"Mean last 3 numbers = {mean}")
   print(f"Mean last 3 numbers = {round(mean,2)}")
