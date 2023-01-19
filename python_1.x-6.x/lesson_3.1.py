# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint as rand

def CreateArray(size):
    max = (size * 3) >> 2
    array = [rand(0, max) for i in range(size)]
    return array

def SumToOddIndex(array, position = 1):
    sum = 0
    for i in range(position, len(array), 2):
        sum += array[i]
    
    return sum


array1 = CreateArray(10)
print(array1)
print(f"Сумма элементов заданного массива, находящихся на нечетных позициях: {SumToOddIndex(array1)}")
#print(f"Сумма элементов заданного массива, находящихся на четных позициях: {SumToOddIndex(array1, 0)}")