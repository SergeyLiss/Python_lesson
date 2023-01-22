interface = [   "\t0 - Открыть/Создать телефонную книгу",
                "\t1 - Создать контакт",
                "\t2 - Изменить контакт",
                "\t3 - Удалить контакт",
                "\t4 - Вывести список контактов",
                "\t5 - Вывести контакт",
                "\t6 - Удалить телефонную книгу",
                "\t7 - Импорт в *.txt" ]
chapter = ["Имя: ", "Фамилия:", "Номер:", "Коммент:"]

def ViewNumbers(pb_list):
    print("id", end= " ")
    for j in range(4):
        print(f" {chapter[j]}", end= " ")
    print()
    for i in range(len(pb_list)):
        temp = pb_list[i].split(";")
        print(i, end= " ")
        for j in range(len(temp)):
            print(f"{temp[j]}", end= " ")
    pass

def ViewNumber(pb_contact):
    pb_contact = pb_contact.split(";")

    for i in range(len(pb_contact)):
        print(f"\t{chapter[i]} {pb_contact[i]}")
    
    pass