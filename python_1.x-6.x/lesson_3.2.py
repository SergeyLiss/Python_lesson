# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint as rand

def CreateArray(size):
    array = [rand(0, size) for i in range(size)]
    return array

def MultiplyToIndex(array):
    sizeOut = (len(array) + 1) >> 1
    arrayOut = [0 for i in range(sizeOut)]

    for i in range(sizeOut):
        arrayOut[i] = array[-i-1] * array[i]
        #print(array[-i], array[i], arrayOut[i], i, -i)
    
    return arrayOut

array1 = CreateArray(9)
array2 = MultiplyToIndex(array1)
print(array1)
print(array2)
