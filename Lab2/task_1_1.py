# 1. Удалить в списке все числа, которые повторяются более двух раз.

myArr = list(map(int,input('Введите числа через пробел\n').split()))

for i in myArr:
    if myArr.count(i)>2:
        myArr.remove(i)

print(myArr)

# 2. Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.

