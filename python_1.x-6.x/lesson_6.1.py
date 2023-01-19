# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: a_n = a_1 + (n-1) * d.
# Каждое число вводится с новой строки.

def Form_AP(array):
    arif_series = [array[0]]

    for i in range((array[2]-1)):
        arif_series.append((arif_series[-1]+array[1]))
    
    return arif_series


def Input_AP():
    arifm = [0,0,0]
    stroki = ['первый элемент','разность','количество элементов']
    for i in range(3):
        arifm[i] = int(input(f'Введите {stroki[i]} арифметической погрешности: '))
    
    return arifm

print(Form_AP(Input_AP()))