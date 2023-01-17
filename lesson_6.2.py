# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint as rand
array1 = [rand(-10, 20) for i in range(20)]

def InputLim():
    limit = [0,0]
    strok = ['минимум','максимум']
    for i in range(2):
        limit[i] = int(input(f'Введите {strok[i]} : '))
    
    return limit

def IndexLimit(array, limit):
    result = []

    for i in range(len(array)):
        if (array[i] >= limit[0]) & (array[i] <= limit[1]):
            result.append(i)
    
    return result
print(array1)
print(IndexLimit(array1, InputLim()))