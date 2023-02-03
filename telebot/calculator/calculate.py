#

class TBCalc():

    def __init__(self):
        # self.const = {'π': 3.14159265359, 'e': 2.71828182846}
        # self.operand_list = ['+', '-', '*', '%', '/', 'xⁿ', '1/x', 'x²', '√x', '=']
        self.operand_list = ['+', '-', '*', '%', '/', 'xⁿ', '=']
        self.number_1 = ' '
        self.number_2 = ' '
        self.operand = ' '
        self.otvet = '0'
        self.flag = True
        self.compl = True
        pass

    def __call__(self):
        # self.ConvertNumber()
        if self.number_1 != ' ':
            self.number_1 = self.Dual(self.number_1)
        self.number_2 = self.Dual(self.number_2)

        if self.operand == self.operand_list[0]:
            self.number_2 = self.number_1 + self.number_2
        elif self.operand == self.operand_list[1]:
            self.number_2 = self.number_1 - self.number_2
        elif self.operand == self.operand_list[2]:
            self.number_2 = self.number_1 * self.number_2
        elif self.operand == self.operand_list[3]:
            self.number_2 = self.number_1 % self.number_2
        elif self.operand == self.operand_list[4]:
            self.number_2 = self.number_1 / self.number_2
        elif self.operand == self.operand_list[5]:
            self.number_2 = pow(self.number_1, self.number_2)
        # elif self.operand == self.operand_list[6]:
        #     self.number_2 = 1 / self.number_2
        # elif self.operand == self.operand_list[7]:
        #     self.number_2 = self.number_2 * self.number_2
        # elif self.operand == self.operand_list[8]:
        #     self.number_2 = pow(self.number_2, 0.5)
        elif self.operand == self.operand_list[6]:
            self.number_2 = self.number_2
        else:
            self.number_2 = 'Такая операция отсутствует'
        
        if self.number_1 != ' ':
            self.number_1 = self.ReDual(self.number_1)
        self.number_2 = self.ReDual(self.number_2)
        return self.number_2
    
    # def ConvertNumber(self):
    #     self.number_1 = self.const[self.number_1] if self.number_1 in self.const else self.Dual(self.number_1)
    #     self.number_2 = self.const[self.number_2] if self.number_2 in self.const else self.Dual(self.number_2)
    
    def ReDual(self, number):
        if isinstance(number, complex):
            print(f'{number}')
            number = f'{number}'.split(self.operand_list[0])
            number = number[0][1:] + '+i' + number[1][:(-2)]
        else:
            number = f'{number}'
            if number[(-2):] == '.0':
                number = number[:(-2)]
        
        return number
    
    def Dual(self, number):
        if 'i' in number:
            number = number.split(self.operand_list[0])
            number = complex(float(number[0]), \
                            float(number[1].replace('i','')))
        else:
            number = float(number)
        
        return number

# test = TBCalc()
# test.number_1 = input("1:")
# test.number_2 = input("2:")
# test.operand = input('=:')
# print(test())
