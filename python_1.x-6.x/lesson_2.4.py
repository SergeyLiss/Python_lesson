#0
#4
#7
#
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = 5
def Multiplication(n):
    array = [i for i in range((-n), (n+1))]

    amount = 3
    amount *= 3

    file = open('python\lesson_2.4.py', 'r')
    multarray = file.read(amount)
    file.close()
    print(multarray)

    multarray = multarray.replace("\n", "")
    size = multarray.count("#")
    quantity = []

    for i in range(len(multarray)):
        if multarray[i] == "#":
            quantity += [i]
    quantity += [len(multarray)]
    
    for i in range(size):
        quantity[i] += 1
        quantity[i] = int(multarray[quantity[i]:quantity[i+1]])

    multplc = 1
    for i in range(size):
        multplc *= array[quantity[i]]
    
    print(f"Произведение элементов на указанных позициях: {multplc}")

Multiplication(5)