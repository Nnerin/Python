# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.
import random
import numpy as np

A = np.array([[2,1,5,-4], [1,6,3,-9], [5,3,8,7], [-4,-9,7,3]])
print(A)
print("----------")
h=('')
for k in range(len(A)):
    for l in range(1,len(A)):
        if A[k][l]!=A[l][k]:
            h=('False')
            break
if h!=('False'):
    print('Матрица симметричная\n')
else:
    print('Матрица несимметричная\n')

A = np.array([[1,2,5,-4], [1,6,3,-9], [5,3,8,7], [-4,-9,7,3]])
print(A)
print("----------")
h=('')
for k in range(len(A)):
    for l in range(1,len(A)):
        if A[k][l]!=A[l][k]:
            h=('False')
            break
if h!=('False'):
    print('Матрица симметричная\n')
else:
    print('Матрица несимметричная\n')

# n=int(input('Введите кол-во строк и столбцов матрицы: '))
# h=('')
# matrix=[[random.randrange(10) for i in range(n)] for j in range(n)]
# for elem in matrix:
#     print(elem)
# for k in range(n):
#     for l in range(1,n):
#         if matrix[k][l]!=matrix[l][k]:
#             h=('False')
#             break
# if h!=('False'):
#     print('Матрица симметрична')
# else:
#     print('Обычная матрица')
