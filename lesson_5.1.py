# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
from random import choices as chaki

abc = ['абв', 'где', ', ', '. ', 'как', 'что', '! ', '? ']
array1 = ''.join(chaki(abc, k=42))

letters = "абв"

array2 = ' '.join(filter(lambda x: not letters in x, array1.split()))

print(array1)
print(array2)
