# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from tkinter import *
from random import randint as rand

class Sweets(Frame):

    def __init__(self) -> None:
        super().__init__()
        self.level = ["Easy", "Hard"] # Сложность игры
        self.statusbar = "" # Строка состояния
        self.field = ""
        self.level_game = 0 # Сложность игры
        self.grafic_positions = [0 for i in range(9)] # Константы игрового поля
        self.step = True # Ход игрока/бота
        self.player = 0 # Счет игрока
        self.bot = 0 # Счет бота
        self.initUI()
        # self.CreateField()
        # self.NewGame()
        
    def initUI(self): # Создание окна + расположение объектов
        # Window
        self.master.title("Candy Game")
        window = self.Monitor() # Размеры окна игры
        self.grafic_positions[0] = window[2]
        self.grafic_positions[1] = window[3]
        self.master.geometry(f"{window[2]}x{window[3]+20}+{window[0]}+{window[1]}")
        self.master.resizable(False, False)
        self.field = Canvas(width=window[2], height=window[3], bg='white')
        self.field.bind("<MouseWheel>", self.WalkPlayer)
        self.field.pack()
        
        # Панель управления
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        var = IntVar()
        submenubar = Menu(menubar)

        menubar.add_cascade(label="Уровень игры", menu=submenubar)
        for i in range(2):
            submenubar.add_command(label=self.level[i], command=lambda x=i : self.Change_statusbar(x))

        # menubar.add_command(label="Новая игра", command=self.NewGame)

        # Строка состояния - нижняя
        self.statusbar = Label(self.master, text="+Уровень сложности: "+self.level[self.level_game], bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
        pass

    def Change_statusbar(self, status): # Изменение сложности игры
        self.statusbar['text'] = "+Уровень сложности: " + self.level[status]
        self.level_game = status
        self.NewGame()
        pass

    def WalkPlayer(self, event):
        print(event.delta)
    
    def Monitor(self): # Расчет оптимального размера окна (игрового поля) и расположения в центре
        mounting = [0,0,0,0]
        mounting[2] = self.master.winfo_screenwidth() >> 2
        mounting[3] = self.master.winfo_screenheight() >> 1
        mounting[0] = ((mounting[2] << 1) + mounting[2]) >> 1
        mounting[1] = mounting[3] >> 1
        return mounting


def main():
    root = Sweets()
    root.mainloop()

if __name__ == '__main__':
    main()