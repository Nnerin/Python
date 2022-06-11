# Task 4.
# По номеру месяца напечатать пору года.

Monthes = ['January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December']

i = int(input("Enter month's number:\n"))
if i > 0 and i <= 12:
    print(f"Your choice: {Monthes[i-1]}")
    if i == 12 or (i > 0 and i < 3):
        print("Season: Winter")
    elif i >= 3 and i < 6:
        print("Season: Spring")
    elif i >= 6 and i < 9:
        print("Season: Summer")
    elif i >= 9 and i < 12:
        print("Season: Autumn")
else:
    print("Number is not correct!")
