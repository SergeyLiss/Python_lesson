# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def SumNumber():
    dictionary = {str(i): i for i in range(10)}
    n = str(input("Введите число: "))
    summa = 0
    for i in n:
        if i in dictionary:
            summa += dictionary[i]
    print(f"Сумма цифр числа: {summa}")


SumNumber()

