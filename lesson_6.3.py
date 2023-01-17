# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# Вариант 1
def RecursExt(a,b):
    if b > 1:
        return a*RecursExt(a,(b-1))
    else:
        return a
# Вариант 2
def Extent(a,b):
    if b > 1:
        c = Extent(a, (b >> 1))
        c *= c
        if b&1:
           c *= a
        
        return c
    else:
        return a 


a = 99
b = 99
print(Extent(a,b))
print(RecursExt(a,b))
