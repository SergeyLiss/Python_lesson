# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint as rand

def CreateArray(size):
    max = (size * 3) >> 2
    array = [rand(0, max) for i in range(size)]
    return array

def RemoveRepeat(array):
    dictionary = {}
    
    for i in array:
        if not (i in dictionary):
            dictionary[i] = 1
    
    array_sort = []
    for i in set(dictionary):
        array_sort += [i]
    
    return array_sort


array1 = CreateArray(10)
array2 = RemoveRepeat(array1)

print(array1)
print(array2)