# Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.

def ExpArray():
    n = int(input("Введите число: ")) + 1
    array = [Exponent(i+1) for i in range(n)]
    summa = 0
    for i in array:
        summa += i
    
    print(array)
    print(summa)

def Exponent(e):
    x = 1 / e
    x += 1
    x = pow(x,e)
    return round(x, 2)

ExpArray()