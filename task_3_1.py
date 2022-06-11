# Task 1.
# Удалить элемент с введенным номером a.
import random

arrSize = int(input("Введите кол-во чисел в массиве: "))
A = []
for i in range(arrSize):
   a = random.randint(0, 100)
   A.append(a)
# for i in range(arrSize):
#     print(A[i])
print("  ".join(map(str, A)))

myNum= int(input(f"Введите номер элемента от 1 до {arrSize}:  "))
if myNum <= 0 or myNum > arrSize:
    print("You input incorrect number!")
else:
    A.pop(int(myNum)-1)
    arrSize = len(A)
    # for i in range(arrSize):
    #     print(A[i])
    print("  ".join(map(str, A)))
