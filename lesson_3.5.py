# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = 8

def NegaFibonacci(num): # Реализация 1
    array = [0 for i in range((num<<1)+1)]
    array[num+1] = 1
    array[num-1] = 1

    for i in range(2, (num+1)):
        array[num+i] = array[num+i-1] + array[num+i-2]
        array[num-i] = array[num+i] if (i&1) == True else -array[num+i]

    return array

def Fibonachi(number): # Реализация 2
    f = 1.6180339887498948482045868343656 # Золотое сечение
    fresult = int((pow(f,number) - pow(-f, -number)) / (2 * f - 1)) # Формула Бине
    return fresult


farray = [Fibonachi(i) for i in range(-number, (number+1))]

print(NegaFibonacci(number))
print(farray)