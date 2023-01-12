# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def DayOfWeek(number):
    if 0 < number < 8:
        if number < 6:
            print(f"{number} <- будний день.")
        else:
            print(f"{number} <- выходной день.")
        return True
    else:
        print(f"{number} <- значение за пределами дней недели.")
        return False

def InputNumber():
    
    n = int(input("Введите число: "))
    m = DayOfWeek(n)
    
    if m == False:
        print("Значение за пределами дней недели. Введите еще раз:")
        InputNumber()


InputNumber()
