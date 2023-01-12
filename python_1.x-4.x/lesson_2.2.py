# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def FactorArray():
    n = int(input("Введите число: ")) + 1
    array = [1]
    for i in range(2,n):
        array += [i*array[-1]]
    print(array)

FactorArray()