# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
keys = '0123456789abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'

def Koding(text):
    textout = text[0]
    count = 1

    for i in text[1:]:
        if textout[-1] == i:
            count += 1
        else:
            textout += keys[count] + i
            count = 1

    textout += keys[count]

    return textout

def Dekoding(text):
    textout = ''

    for i in range(0, len(text), 2):
        count = 0
        
        for j in range(60):
            if keys[j] == text[i+1]:
                count = j
                break
        
        for k in range(count):
            textout += text[i]
        
    return textout

text_in = '111111111ddddddddd4444444444eeeeeeeeeeeeeeeeee5w444ssssssss11111a7777sssssss545xccccccccQQQQQQ'
text_kod = Koding(text_in)
text_dekod = Dekoding(text_kod)

print(f'{text_in}\n\n{text_kod}\n\n{text_dekod}')
