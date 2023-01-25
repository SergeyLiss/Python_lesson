interface = [   "\t0 - Сгенерировать 'школу' ",
                "\t1 - Добавить нового студента",
                "\t2 - Добавить предмет",
                "\t3 - Добавить оценку ученику по предмету",
                "\t4 - Показать список учеников",
                "\t5 - Показать лист оценок ученика",
                "\t6 - Вывод средней оценки ученика по одному предмету",
                "\t7 - Вывод среднего балла по школе по конкретному предмету",
                "\t8 - Вывод количества учеников претендующих на золотую медаль",
                "\t9 - Генерация оценок",
                "\t(любая) - Выход из программы" ]

def PrintList(table, flag=False):
    for i in range(len(table)):
        print(end='\t')
        if flag:
            print(f'{i} --->', end=' ')
        print(f'{table[i]}')
    
    if flag:
        ch = ''
        while ch == '':
            ch = input("Введите индекс: ")
        
        return int(ch)

def PrintClasses(table):
    for i in range(len(table)):
        print(f"{i+7} класс:")
        PrintList(table[i])

def ListAssessmant(assessmant, student, lesson):
    nm = ''
    while nm == '':
        nm = input("Выберете номер класса (7-9): ")
        nm = int(nm)

    print(f"{nm} класс:")
    ns = PrintList(student[nm%7], True)
    print(f'Лист оценок ученика(цы) {nm} класса - {student[nm%7][ns]}:')
    for i in range((nm%7)):
        ns += len(student[i])
    
    for i in range(len(lesson)):
        print(f'\t{lesson[i]}:', end=' ')
        for j in range(len(assessmant[ns][i])):
            if assessmant[ns][i][j] != 0:
                print(assessmant[ns][i][j], end=', ')
        print()
            
def MediumAssesmantStudent(assessmant, student, lesson):
    nm = ''
    while nm == '':
        nm = input("Выберете номер класса (7-9): ")
        nm = int(nm) % 7

    print(f"{nm} класс:")
    ns = PrintList(student[nm], True)
    print("Список предметов:")
    nl = PrintList(lesson, True)

    print(f'Средняя оценка ученика(цы) {nm+7} класса - {student[nm][ns]} по {lesson[nl]}:', end=' ')
    for i in range(nm):
        ns += len(student[i])
    
    medium = 0
    size = 0
    for i in assessmant[ns][nl]:
        if i != 0:
            medium += i
            size += 1
    
    print(f'{(medium/size)}')

def MediumAssesmantLesson(assessmant, student, lesson):
    print("Список предметов:")
    nl = PrintList(lesson, True)

    print(f'Средний балл по школе по {lesson[nl]}:', end=' ')
    medium = 0
    size = 0
    for i in range(len(assessmant)):
        for j in range(len(assessmant[i][nl])):
            if assessmant[i][nl][j] != 0:
                medium += assessmant[i][nl][j]
                size += 1
    
    print(f'{medium/size}')

def GoldenHonor(assessmant, student, lesson):

    print(f'Количество учеников претендующих на золотую медаль:', end=' ')
    kolvo = 0
    for i in assessmant:
        medium = 0
        size = 0
        for j in i:
            for k in j:
                if k != 0:
                    size +=1
                if k >= 4:
                    medium += 1
        
        if medium == size:
            kolvo += 1

    print(f'{kolvo}')