# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 3628800

def Factorization(n):
    factor = {}

    if not(n&1) :
        factor[2] = 0
    while not(n&1):
        factor[2] += 1
        n >>= 1
    
    rootn = int(pow(n, 0.5) + 1)
    divider = 1

    while (n != 1) and (divider < rootn):
        divider += 2
        if (n%divider) == 0:
            if divider in factor:
                factor[divider] += 1
            else:
                factor[divider] = 1
            
            n //= divider
            divider -= 2
    
    if n != 1:
        factor[n] = 1

    return factor

def PrintFactor(n):
    print(f"Множители числа {n}:")

    for i in Factorization(n):
        print(f"{i}^{Factorization(n)[i]}", end=" ")
    
PrintFactor(n)