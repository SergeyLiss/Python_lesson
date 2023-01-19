# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def Coordinates():
    coordinat = ["A_x", "A_y", "B_x", "B_y"]

    for i in range(4):
        coordinat[i] = int(input(f"Введите {coordinat[i]}: "))
    
    distance = pow((coordinat[0] - coordinat[2]),2)
    distance += pow((coordinat[1] - coordinat[3]),2)
    distance = round(pow(distance, 0.5),2)
    
    print(f"Расстояние между точками A({coordinat[0]};{coordinat[1]}) и B({coordinat[2]};{coordinat[3]}) равняется {distance}.")

Coordinates()

