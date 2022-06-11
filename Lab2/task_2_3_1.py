# Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме элементов,
# стоящих на том же месте в 1-й и 2-й таблицах.
import random
import numpy as np

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
An1 = np.array(A1)
print("First array:")
print(An1)
print()

for i in range(arrSize):
    B = []
    for j in range(arrSize):
        a = random.randint(0, 100)
        B.append(a)
    A2.append(B)
An2 = np.array(A2)
print("Second array:")
print(An2)
print("======================")
print()
A3 = An1 + An2
print(A3)