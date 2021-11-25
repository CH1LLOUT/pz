import math
a = int(input("Введите чило a: "))
b = int(input("Введите чило b: "))
s = str
if a < b:
    for x in range(a, b + 1):
        s = str(x)
        print(s*(x-a+1))

else:
    print("Введите числа a и b занаво, при условии что a < b")

