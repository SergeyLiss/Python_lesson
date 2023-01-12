# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = 6011258499

def ToBin(num):
    strbin = ""

    while num != 0:
        i = num & 1
        strbin = str(i) + strbin
        num >>= 1
    
    return("0b" + strbin)

print(ToBin(number))
print(bin(number))
    
