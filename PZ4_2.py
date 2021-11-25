N = int(input("Введите положительное число n: "))
K = int(input("Введите положительное число k: "))
a = 0
if N >= K:
    while N >= K:
        a += 1
        N -= K
    print("Частоное от деления: " + str(a) + "  Остаток от деления : " + str(N))
else:
    print("o")