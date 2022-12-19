# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = 8

def NegaFibonacci(num):
    array = [0 for i in range((num<<1)+1)]
    array[num+1] = 1
    array[num-1] = 1

    for i in range(2, (num+1)):
        array[num+i] = array[num+i-1] + array[num+i-2]
        array[num-i] = array[num+i] if (i&1) == True else -array[num+i]

    return array

print(NegaFibonacci(number))