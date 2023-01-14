# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

f = open("qwerty.txt", "r", encoding="utf8")
q = ''.join(f.readlines())
d = {}
for i in q:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
a = list(set(d.values()))

print(a)