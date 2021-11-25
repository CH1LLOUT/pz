import math
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
if 0 < x1 < 9 and 0 < x2 < 9 and 0 < y1 < 9 and 0 < y2 < 9:
    if x1 == x2 or y2 == y1:
        print("true")
    else :
        print("false")
else:
    print("Числа не попадают в диапозон")
