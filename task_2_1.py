# Task 1.
# Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7. Могут ли два билета подряд быть удачными?
# 069999

num1 = list(map(int, input("Add ticket's number: ").split()))
#print(num1)
sum = 0
for i in range(len(num1)):
    sum += num1[i]
print(f"sum 1 ticket = {sum}")
num = int(''.join([str(i) for i in num1]))+1
#print(num)

num2 = list(str(num))
#print(num2)

sum2 = 0
for i in range(len(num2)):
    sum2 += int(num2[i])
print(f"sum 2 ticket = {sum2}")
print("========================")
if sum % 7 == 0 and sum2 % 7 == 0:
    print("2 tickets are happy!")

else:
    print(f"1st ticket sum: {sum}")
    print(sum % 7)
    print(f"2nd ticket sum: {sum2}")
    print((sum2) % 7)

# Вывод всех билетов.

# for i1 in range(0,10, 1):
#     for i2 in range(0, 10, 1):
#         for i3 in range(0, 10, 1):
#             for i4 in range(0, 10, 1):
#                 for i5 in range(0, 10, 1):
#                     for i6 in range(0, 10, 1):
#                         if (i1+i2+i3+i4+i5+i6) % 7 ==0:
#                             print(f"ticket {i1}{i2}{i3}{i4}{i5}{i6} is happy!")
