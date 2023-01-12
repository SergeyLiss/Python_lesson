# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint as rand

k = 10000

def Polynomial(k):
    polyx = ""

    for i in range(k):
        polyx += str(rand(0,100)) + " x^" + str((k-i)) + " + "
    
    polyx += str(rand(0,100)) + " = 0"

    print(polyx)

    return polyx

def PolynomToFile(k):
    f = open("poly_file.txt", "w")
    f.write(Polynomial(k))
    f.close()

PolynomToFile(k)
    