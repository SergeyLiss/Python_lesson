# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def QuarterNumber():
    print("Введите номер четверти.")
    q = int(input("Введите Q: "))
    if 0 < q < 5:
        print(f"В {q} четверти оси могут принимать следующие значения:")
        if((q%4) < 2):
            print("X: от 0 до бесконечности, при x > 0")
        else:
            print("X: от 0 до бесконечности, при x < 0")
        
        if(q < 3):
            print("Y: от 0 до бесконечности, при y > 0")
        else:
            print("Y: от 0 до бесконечности, при y < 0")
    else:
        print(f"{q} <- значение за пределами из 4 возможных четвертей.")

QuarterNumber()