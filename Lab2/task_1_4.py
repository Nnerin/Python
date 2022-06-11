# 1. Найдите произведение элементов списка с нечетными номерами.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 10)
   A.append(a)
print("  ".join(map(str, A)))

multNum = 1
for i in range(1, arrSize, 2):
    multNum *= A[i]

print(f"произведение элементов списка с нечетными номерами: {multNum}")

# 2. Найдите наибольший элемент списка, затем удалите его и выведите новый список.
print("================================\n")

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
B = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))

maxNum = max(A)
print(f"Максимальное число в массиве: {maxNum}")

B = list(A)
B.remove(max(B))
print("  ".join(map(str, B)))