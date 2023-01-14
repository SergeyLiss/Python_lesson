#
from tkinter import *
from random import randint as rand

# tic-tac-toe
class T3(Frame):

    def __init__(self) -> None:
        super().__init__()
        self.level = ["Стандартный", "Посложней", "Безграничный"] # Сложности игры
        self.statusbar = [] # Строка состояния
        self.level_game = 0 # Сложность игры
        self.field = ""
        self.grafic_positions = [0 for i in range(9)] # Константы игрового поля
        self.step = True # Ход игрока/бота
        self.player = 0 # Позиции игрока
        self.bot = 0 # Позиции бота
        self.steps = 0 # Количество ходов
        self.zona = [] # Позиции в занятых клеток в игре
        self.chek = [ 0x7, 0x38, 0x49, 0x54, 0x92, 0x111, 0x124, 0x1c0] # Условия победы
        self.initUI()
        self.CreateField()
        self.NewGame()
        
    def initUI(self): # Создание окна + расположение объектов
        # Window
        self.master.title("Крестики-нолики")
        window = self.Monitor() # Размеры окна игры
        self.grafic_positions[0] = window[2]
        self.grafic_positions[1] = window[3]
        self.master.geometry(f"{window[2]}x{window[3]+20}+{window[0]}+{window[1]}")
        self.master.resizable(False, False)
        self.field = Canvas(width=window[2], height=window[3], bg='white')
        self.field.bind('<Button-1>', self.WalkPlayer)
        self.field.pack()
        
        # Панель управления
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        var = IntVar()
        submenubar = Menu(menubar)

        menubar.add_cascade(label="Уровень игры", menu=submenubar)
        for i in range(3):
            submenubar.add_command(label=self.level[i], command=lambda x=i : self.Change_statusbar(x))

        menubar.add_command(label="Новая игра", command=self.NewGame)

        # Строка состояния - нижняя
        self.statusbar = Label(self.master, text="+Уровень сложности: "+self.level[self.level_game], bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
        pass
    
    def Monitor(self): # Расчет оптимального размера окна (игрового поля) и расположения в центре
        mounting = [0,0,0,0]
        mounting[2] = self.master.winfo_screenwidth() >> 2
        mounting[3] = self.master.winfo_screenheight() >> 1
        mounting[0] = ((mounting[2] << 1) + mounting[2]) >> 1
        mounting[1] = mounting[3] >> 1
        return mounting
    
    def Change_statusbar(self, status): # Изменение сложности игры
        self.statusbar['text'] = "+Уровень сложности: " + self.level[status]
        self.level_game = status
        pass

    def CalcField(self): # Расчет основных констант игрового поля
        self.grafic_positions[2] = self.grafic_positions[0] // 5 #
        self.grafic_positions[3] = self.grafic_positions[1] // 5 #
        temp = min(self.grafic_positions[2], self.grafic_positions[3]) // 2 # Минимальное значение от (высоты, ширины)
        self.grafic_positions[4] = temp -  (temp % 20) # Больший радиус нолика
        self.grafic_positions[5] = (self.grafic_positions[4] << 2) // 5 # Максимальная длина луча 
        self.grafic_positions[6] = 10 # Толщина нолика
        self.grafic_positions[7] = 5 # Толщина крестика
        self.grafic_positions[8] = 1 # Толщина линий сетки игрового поля

    def CreateField(self): # Создание сетки поля
        self.CalcField()

        const = self.grafic_positions[8]
        a = self.grafic_positions[2]
        b = self.grafic_positions[3]
        
        self.field.create_rectangle(a,(2*b-const),(4*a),(2*b+const),fill="black")
        self.field.create_rectangle(a,(3*b-const),(4*a),(3*b+const),fill="black")
        self.field.create_rectangle((2*a-const),b,(2*a+const),(4*b),fill="black")
        self.field.create_rectangle((3*a-const),b,(3*a+const),(4*b),fill="black")
        pass
    
    def CreateCircle(self, centerx, centery): # Русуем нолик
        const = self.grafic_positions[6]
        a1 = centerx+self.grafic_positions[4]
        a2 = centery+self.grafic_positions[4]
        b1 = centerx-self.grafic_positions[4]
        b2 = centery-self.grafic_positions[4]
        # O
        self.field.create_oval(a1, a2, b1, b2, fill='green', tags='game')
        self.field.create_oval((a1-const), (a2-const), (b1+const), (b2+const), fill='white', tags='game')
        pass
    
    def CreateCross(self, centerx, centery): # Рисуем крестик
        const = self.grafic_positions[7]
        a1 = centerx+self.grafic_positions[5]+const
        a2 = centery+self.grafic_positions[5]-const
        b1 = centerx+self.grafic_positions[5]-const
        b2 = centery+self.grafic_positions[5]+const
        c1 = centerx-self.grafic_positions[5]-const
        c2 = centery-self.grafic_positions[5]+const
        d1 = centerx-self.grafic_positions[5]+const
        d2 = centery-self.grafic_positions[5]-const
        # /
        points = [a1,a2,b1,b2,c1,c2,d1,d2]
        self.field.create_polygon(points, fill='blue', tags='game')
        # \
        points = [d1,b2,c1,a2,b1,d2,a1,c2]
        self.field.create_polygon(points, fill='blue', tags='game')
        pass

    def NewGame(self): # Новая игра
        self.field.delete('game')
        self.step = True
        self.player = 0
        self.bot = 0
        self.steps = 0
        self.zona = [[-1,-1,-1,-1,-1],
                        [-1,0,0,0,-1],
                        [-1,0,0,0,-1],
                        [-1,0,0,0,-1],
                        [-1,-1,-1,-1,-1]]
        pass
    
    def WalkPlayer(self, event): # Обработка хода игрока
        if self.steps < 9:
            a = event.x // self.grafic_positions[2]
            b = event.y // self.grafic_positions[3]
            if self.zona[a][b] == 0:
                self.steps += 1
                self.Fillin(a, b)
                self.step = False
                if self.WinToWin():
                    self.steps = 9
                    self.WinGame("Player Win")
                else:
                    self.WalkBot()
        # else:
        #     self.WinGame("Ничья")
        pass

    def Fillin(self, posx, posy): # Обноление счета, вызов печати фигуры
        temp = (1 << ((posx-1)*3+(posy-1)))
        self.zona[posx][posy] = 1
        posx, posy = self.MediumPosition(posx,posy)
        if self.step:
            self.CreateCross(posx,posy)
            self.player ^= temp
        else:
            self.CreateCircle(posx,posy)
            self.bot ^= temp
        pass

    def MediumPosition(self, x, y): # Расчет центра позиции
        x = (x << 1) + 1
        x *= self.grafic_positions[2] >> 1
        y = (y << 1) + 1
        y *= self.grafic_positions[3] >> 1
        return x, y

    def WalkBot(self): # Ход бота
        if self.level_game == 0:
            if self.steps < 9:
                self.steps += 1
                a, b = rand(1,3), rand(1,3)
                while self.zona[a][b] != 0:
                    a, b = rand(1,3), rand(1,3)
                self.Fillin(a,b)
                self.step = True
                if self.WinToWin():
                    self.steps = 9
                    self.WinGame("Bot Win")
            else:
                self.WinGame("Ничья")
        else:
            self.steps = 9
            self.WinGame("Данный уровень в разработке :)")
        pass
    
    def WinToWin(self): # Проверка условий победы
        if self.step:
            for i in self.chek:
                j = self.bot & i
                if j == i:
                    return True

        else:
            for i in self.chek:
                j = self.player & i
                if j == i:
                    return True
        return False
    
    def WinGame(self, txt): # Вывод информации о матче
        
        a = self.grafic_positions[0] >> 1
        b = self.grafic_positions[3] >> 1
        self.field.create_text(a,b, text=txt, font='Arial 20', tags='game')
        pass