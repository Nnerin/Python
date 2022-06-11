# Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме элементов,
# стоящих на том же месте в 1-й и 2-й таблицах.
import random

arrSize = int(input("Введите размерность массива: \n"))
A1 = []
A2 = []
A3 = []
for i in range(arrSize):
    B = []
    for j in range(arrSize):
        a = random.randint(0, 100)
        B.append(a)
    A1.append(B)
print("  ".join(map(str, A1)))
for i in range(arrSize):
    B = []
    for j in range(arrSize):
        a = random.randint(0, 100)
        B.append(a)
    A2.append(B)
print("  ".join(map(str, A2)))
print("======================")

for i in range(arrSize):
    for j in range(arrSize):
        print(A1[i][j], end =" ")
    print()
print("*******")
for i in range(arrSize):
    for j in range(arrSize):
        print(A2[i][j], end =" ")
    print()
print("======================")

for i in range(arrSize):
    B = []
    for j in range(arrSize):
        a = A1[i][j]+A2[i][j]
        B.append(a)
    A3.append(B)
for i in range(arrSize):
    for j in range(arrSize):
        print(A3[i][j], end =" ")
    print()