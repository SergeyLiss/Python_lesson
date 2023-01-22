from file.log import *
from io_user.action_user import *
from io_user.view import *
from file.im_ex_port import *

log_file = "python/phonebook/data/log.txt"
pb_file = "python/phonebook/data/"

pb = ActionUser(pb_file)
l = Logg(log_file)

def InputId():
    pos = ""
    while pos.isnumeric() != True:
        pos = input("Введите id контакта: ")
    return int(pos)

def Deistvie():
    flag = True
    while flag != False:
        print("Выберите действие:")
        for i in interface:
            print(i)
        
        ch = input()
        
        if ch == '0':
            name = input(f"Введите имя телефонной книги: ")
            if name == "":
                name = "my_phonebook"
            pb.path_bd = pb_file + name + ".csv"
            pb.ReadBD()
            l.text = f"open/create phonebook={name}.csv"
        elif ch == '1':
            pb.id_number = len(pb.lines)
            pb.CreateNumber()
            l.text = f"create id={pb.id_number}"
        elif ch == '2':
            pb.id_number = InputId()
            pb.ChangeNumber()
            l.text = f"change id={pb.id_number}"
        elif ch == '3':
            pb.id_number = InputId()
            pb.DeleteNumber()
            l.text = f"delete id={pb.id_number}"
        elif ch == '4':
            ViewNumbers(pb.lines)
        elif ch == '5':
            pos = InputId()
            if pos < len(pb.lines):
                ViewNumber(pb.lines[pos])
            else:
                print("Введеный id несуществует.")
        elif ch == '6':
            pb.DeleteBD()
            l.text = "delete phonebook"
        elif ch == '7':
            Import(pb.lines, (pb.path_bd[:(-4)] + '.txt'))
            l.text = "delete phonebook"
        else:
            pb.ChangeBD()
            flag = False
            print("Телефонная книга закрыта")
            l.text = "close phonebook"
        l.Logger()
    
