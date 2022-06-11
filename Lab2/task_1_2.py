# 1. Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
B = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))

for i in range(arrSize):
   if A[i] % 2 != 0:
      B.append(A[i])
#print (B)
if len(B) == 0:
   print("В массиве нет нечетных чисел")
else:
   maxNum = max(B)
   print(f"Максимальное нечетное число: {maxNum}")

# 2. Найдите минимальный по модулю элемент списка.
print("================================\n")

myArr = list(map(int,input('Введите числа через пробел\n').split()))
min_ = float('inf')
for i in range(len(myArr)):
    if abs(myArr[i]) < abs(min_):
        min_ = myArr[i]
print(f"Минимальное по модулю число: {min_}")

