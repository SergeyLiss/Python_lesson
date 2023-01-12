# Реализуйте алгоритм перемешивания списка.
from random import randint as rand

def Search_p(count):
    if (count&1) == 0:
        count += 1
    
    flag = False

    while flag == False:
        flag = True
        count += 2

        for i in range(3, count, 2):
            if(count%i) == 0:
                flag = False
                break
    
    return count

def Search_q(p):
    half = (p-1) >> 1

    flag = False
    q = 0

    while flag == False:
        q = rand(2, (p-2))
        if pow(q, half, p) == (p-1):
            flag = True
        
    return q

def CreateArray(size):
    max = (size * 3) >> 2
    array = [rand(0, max) for i in range(size)]
    return array

def SortArray(array):
    size = len(array)
    p = Search_p(size)
    q = Search_q(p)

    for i in range(size):
        j = pow(q, (2+i), p)

        if (j < size) and (j > i):
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
    
    return array


array1 = CreateArray(10)
print(array1)
array2 = SortArray(array1)
print(array2)


