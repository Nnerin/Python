# Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом и записать эти суммы в новый список B.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))
print("========================")

B = []
for i in range(0, arrSize-1, 2):
    num = A[i]+A[i+1]
    B.append(num)
print("  ".join(map(str, B)))
