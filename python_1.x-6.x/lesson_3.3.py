# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import random as randf

def CreateArray(size):
    array = [round(randf()*10, 2) for i in range(size)]
    return array

def DifferenceIntervalFloat(arrayin):
    max = 0
    min = 1
    for i in arrayin:
        j = i % 1
        if j != 0:
            if j > max:
                max = j
            if j < min:
                min = j
    return (max - min)

array1 = CreateArray(10)
print(array1)
print(round(DifferenceIntervalFloat(array1), 2))
