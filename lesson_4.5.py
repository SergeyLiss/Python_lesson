# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
from random import randint as rand

def Polynomial(k): # Генерируется полином степени k
    polyx = ""

    for i in range(k):
        q = rand(0,100)
        if q != 0:
            polyx += str(q) + "x^" + str((k-i)) + "+"
    
    polyx += str(rand(0,100)) + "=0"

    return polyx

def CreatTwoPolynom(): # Создаются два файла с полиномами со случайными степенями в интервале(1, 100)
    f = open("poly_file_1.txt", "w")
    g = open("poly_file_2.txt", "w")
    f.write(Polynomial(rand(1, 10)))
    g.write(Polynomial(rand(1, 10)))
    f.close()
    g.close()

def SumPolynom(polyn1, polyn2): # Суммирование двух полиномов, представленных в виде словарей, где ключем является степень
    size = max(max(polyn1.keys()), max(polyn2.keys()))
    polynout = ""
    for i in range((size+1)):
        q = 0

        if (size-i) in polyn1:
            q += polyn1[size-i]
        if (size-i) in polyn2:
            q += polyn2[size-i]

        if i != size:
            if q != 0:
                polynout += str(q) + "x^" + str((size-i)) + "+"
        else:
            polynout += str(q) + " = 0"

    return polynout

def ProcessStr(strok): # Преобразовение строк в словари
    strok = strok.replace("x^", " ").replace("+", " ").split()
    strok = [int(strok[i]) for i in range(len(strok))]

    dictionary = {0: strok[-1]}

    for i in range(1, len(strok), 2):
        dictionary[strok[i]] = strok[i-1]

    return dictionary

def SumPolynomToFile(): # Считывание полиномов из файлов и занесение в файл их сумму
    f1 = open("poly_file_1.txt", "r")
    p1 = ProcessStr(f1.readline()[:-2])
    f1.close()
    f2 = open("poly_file_2.txt", "r")
    p2 = ProcessStr(f2.readline()[:-2])
    f2.close()
    f3 = open("poly_file_sum.txt", "w")
    f3.write(SumPolynom(p1,p2))
    f3.close()

CreatTwoPolynom()
SumPolynomToFile()
