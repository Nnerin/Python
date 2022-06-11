# 1. Найдите сумму номеров минимального и максимального элементов.
import random

arrSize = int(input("Введите кол-во чисел в массиве: \n"))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
print("  ".join(map(str, A)))

minNum = min(A)
maxNum = max(A)
sum = A.index(min(A)) + A.index(max(A))
print(f"\nmin = {minNum}")
print(f"max = {maxNum}")
print(f"sum indexes = {sum}")

# 2. По целому n и n положительным целым числам определите, можно ли из них образовать подмножество,
# сумма элементов которого делится на n без остатка. Если можно, то найти любое из таких подмножеств.


