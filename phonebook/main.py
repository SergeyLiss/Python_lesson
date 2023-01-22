from controller import *
from file.spisok import *
from random import randint, choice

def GeneratePhoneBook(size):
    lines = []
    for i in range(size):
        a1 = choice(name_people)
        a2 = choice(lastname_people)
        if a1 in female_name:
            a2 += 'a'
        a3 = '+7 ' + f'{randint(1000000000, 9999999999)}'
        a4 = choice(kategoria)
        a1 = a1 + ';' + a2 + ';' + a3 + ';' + a4 + '\n'
        lines.append(a1)
    
    f = open("python/phonebook/data/my_phonebook.csv", 'w', encoding="utf-8")
    f.writelines(lines)
    f.close()

GeneratePhoneBook(100)
Deistvie()
    