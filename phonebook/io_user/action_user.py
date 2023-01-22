# Действия пользователя
import os

class ActionUser():

    def __init__(self, path_bd, id_number=None) -> None:
        self.path_bd = path_bd
        self.id_number = id_number
        self.lines = []
        self.chapter = ["имя контакта", "фамилия контакта", "номер телефона", "комментарий"]
        pass
    
    def CreateNumber(self):
        entry = ["", "", "", ""]
        for i in range(4):
            while entry[i] == "":
                entry[i] = input(f"Введите {self.chapter[i]}: ")

        entry = ";".join(entry) + "\n"
        
        self.lines.append(entry)
        pass
    
    def ChangeNumber(self):
        entry = self.lines[self.id_number].split(";")
        for i in range(4):
            ch = input(f"Введите {self.chapter[i]}: ")
            if ch != "":
                entry[i] = ch

        self.lines[self.id_number] = ";".join(entry) + "\n"
        pass
    
    def DeleteNumber(self):
        entry = self.lines[self.id_number].split(";")[:2]
        ch = input(f"Вы уверены, что ходите удалить запись {entry[0] + entry[1]} (y/n): ")
        if ch == "y":
            self.lines[self.id_number] = ""
        pass

    def ReadBD(self):
        try:
            file = open(self.path_bd, "r+", encoding="utf-8")
            self.lines = file.readlines()
            file.close()
        except FileNotFoundError:
            print("Телефонной книги с таким именем нет")
            self.CreateBD()
        pass
    
    def CreateBD(self):
        new_file = open(self.path_bd, "w")
        new_file.close()
        print(f"Телефонная книга создана.")
        print(self.path_bd)
        pass

    def ChangeBD(self):
        with open(self.path_bd, "w", encoding="utf-8") as file:
            file.writelines(self.lines)
            file.close()
        pass
    
    def DeleteBD(self):
        file_del = self.path_bd.split("/")[-1]
        ch = input(f"Вы уверены, что ходите удалить телефонную книгу {file_del} (y/n): ")
        if ch == "y":
            os.remove(self.path_bd)
            self.lines = []
            print(f"Телефонная книга {file_del} удалена.")
        pass

