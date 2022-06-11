# Task 2.
# Все четные по значению элементы исходного списка A поместить в новый список B.
import random

arrSize = int(input("Введите кол-во чисел в массиве: "))
A = []
B = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)

for i in range(arrSize):
    print(A[i])
print("=================\n")

for i in range(arrSize):
    if int(A[i]) % 2 == 0:
        num = A[i]
        B.append(num)

arrSizeB = len(B)
if arrSizeB == 0:
    print("Нет четных чисел!")
else:
    for i in range(arrSizeB):
        print(B[i])

# Все элементы четного индекса исходного списка A поместить в новый список B.
#
# arrSize = int(input("Введите кол-во чисел в массиве: "))
# A = []
# B = []
# for i in range(arrSize):
#    a = random.randint(0, 100)
#    A.append(a)
#
# for i in range(arrSize):
#     print(A[i])
# print("=================\n")
#
# B = A[0: arrSize: 2]
#
# arrSizeB = len(B)
# for i in range(arrSizeB):
#     print(B[i])