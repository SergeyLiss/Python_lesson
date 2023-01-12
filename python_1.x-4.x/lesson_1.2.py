# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def QuarterNumber():
    print("Введите координыты точки.")
    x = int(input("Введите X: "))
    y = int(input("Введите Y: "))
    z = 0

    if (x != 0) and (y != 0):
        if x < 0:
            z = 1
        if y < 1:
            z = ~z
        z = (z&3) + 1
        z = "в " + str(z) + " четверти"

    elif (x != 0) or (y != 0):
        if x == 0:
            z = "на оси Y"
        if y == 0:
            z = "на оси X"
    
    else:
        z = "в центре координатной плоскости"

    print(f"Ваша точка({x};{y}) находится {z}.")

QuarterNumber()
    
    