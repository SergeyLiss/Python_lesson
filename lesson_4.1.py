# Вычислить число c заданной точностью d
# Вычисление Пи с заданной точностью, используя формулу Мачина, и ряд Тейлора для арктангенса
import math
from decimal import *

class Pi_Precision():

    def __init__(self, d):
        self.d = d
        getcontext().prec = d
    
    def arctan(self, x):
        x = Decimal(x)
        result = Decimal(0)
        one = 1
        
        for i in range(1, 1024, 2):
            result += one / (i * x ** i)
            one = -one
        
        return result
    
    def pi_arctan(self):
        return 4*(4*self.arctan(5) - self.arctan(239))


d = 100
test = Pi_Precision(d)
pi = test.pi_arctan()
print(f"Pi = {pi}")
  