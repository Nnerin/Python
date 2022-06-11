# В матрице найти номер строки, сумма чисел в которой максимальна.
import random

arrSize = int(input("Введите размерность массива: \n"))
A = []
for i in range(arrSize):
    B = []
    for j in range(arrSize):
        a = random.randint(0, 100)
        B.append(a)
    A.append(B)
print("  ".join(map(str, A)))
print("======================")

for i in range(arrSize):
    for j in range(arrSize):
        print(A[i][j], end =" ")
    print()
max = 0
for i in range(arrSize):
    maxStr = 0
    for j in range(arrSize):
        maxStr += A[i][j]

        if maxStr > max:
            max = maxStr
            nomStr = [i+1]
    print(f"Сумма в строке {[i+1]}: ", maxStr)
print("======================")
print(f"Максимальное значение суммы чсел в строке {nomStr}: ", max)

