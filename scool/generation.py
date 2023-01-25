from random import randint, shuffle, choice
from spisok import *

class Generator():

    def __init__(self) -> None:
        self.study_week = 5 # Учебная неделя из пяти дней
        self.study_class = 3 # Три учебных класса: 7,8,9.
        self.limit_of_lessons = [4,6] # Количество уроков: min/max
        self.limit_of_students = [30,40] # Количество учеников в классе: min/max
        self.limit_days = 100 # Количество учебных дней
        # Импортирование из списков (строка 2)
        self.lessons_list = lessons_list
        self.student_name = name_people
        self.student_lastname = lastname_people
        self.f_name = female_name
        pass

    def GenTable(self): # Генератор расписания уроков
        table_of_lessons = []
        temp_l = len(self.lessons_list)
        for i in range(self.study_class):
            temp_k = [k for k in range(temp_l)]
            temp_k += temp_k
            shuffle(temp_k)
            temp_j = []
            for j in range(self.study_week):
                k = randint(self.limit_of_lessons[0], self.limit_of_lessons[1])
                temp_j.append(temp_k[:k])
                temp_k = temp_k[k:]
            table_of_lessons.append(temp_j)

        self.ToFile(table_of_lessons, "python/scool/data/table_lessons.txt", 3)
        return table_of_lessons
    
    def GenStudent(self): # Генератор студентов
        table_of_students = []
        for i in range(self.study_class):
            temp_i = []
            for j in range(randint(self.limit_of_students[0], self.limit_of_students[1])):
                temp1 = choice(self.student_name)
                temp2 = choice(self.student_lastname)
                if temp1 in self.f_name:
                    temp2 += 'a'
                temp_i.append((temp2 + ' ' + temp1))
            table_of_students.append(sorted(temp_i))
        
        self.ToFile(table_of_students, "python/scool/data/table_students.txt", 2)
        return table_of_students
    
    def ToFile(self, table, path, level): # Запись в файл
        levels = '_.,-'
        with open(path, 'w', encoding='utf-8') as file:
            for i in table:
                file.write(levels[0])
                if 1 < level:
                    for j in i:
                        file.write(levels[1])
                        if 2 < level:
                            for k in j:
                                file.write(levels[2])
                                if 3 < level:
                                    for m in k:
                                        file.write(levels[3])
                                        file.write(f'{m}')
                                else:
                                    file.write(f'{k}')
                        else:
                            file.write(f'{j}')
                else:
                    file.write(f'{i}')
            file.close()
    
    def FromFile(self, path): # Чтение из файла
        levels = '_.,-'
        with open(path, 'r', encoding='utf-8') as file:
            table = file.readlines()[0]
            file.close()

        if table[0] == levels[0]:
            table = table.split(levels[0])[1:]
            if table[0][0] == levels[1]:
                table = [i.split(levels[1])[1:] for i in table]
                if table[0][0][0] == levels[2]:
                    table = [[j.split(levels[2])[1:] for j in i] for i in table]
                    if table[0][0][0][0] == levels[3]:
                        table = [[[k.split(levels[3])[1:] for k in j] for j in i] for i in table]
        return table
    
    def GenAssessment(self, students, lessons): # Генератор оценок
        len_lessons = len(self.lessons_list)
        len_students = 0
        for i in students:
            len_students += len(i)
        
        table_assessmants = [[[0 for k in range(self.limit_days)] for j in range(len_lessons)] for i in range(len_students)]

        len_students = 0
        for i in range(len(students)):
            for j in range(len(students[i])):
                min_assessment = randint(2,4)
                for k in range(len_lessons):
                    for m in range(self.limit_days):
                        day = m % 5
                        if k in lessons[i][day]:
                            table_assessmants[len_students][k][m] = randint(min_assessment, 5)
                len_students += 1
        
        self.ToFile(table_assessmants, "python/scool/data/table_assessmants.txt", 3)
        return table_assessmants
        
                        
