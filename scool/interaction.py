import view

def AddLesson():
    ch = ''
    while ch == '':
        ch = input("Введите название предмета: ")
    return ch

def AddStudent(table):
    nm = ''
    while nm == '':
        nm = input("Введите номер класса, в какой вписать ученика (7-9): ")
        nm = int(nm) % 7
    
    ch = ''
    while ch == '':
        ch = input("Введите имя и фамилию ученика: ")
    
    table[nm].append(ch)
    sorted(table[nm])
    return table

def AddAssessment(assessmant, student, lesson):
    nm = ''
    while nm == '':
        nm = input("Выберете номер класса (7-9): ")
        nm = int(nm)

    print(f"{nm} класс:")
    nm %= 7
    ns = view.PrintList(student[nm], True)
    for i in range(nm):
        ns += len(student[i])

    print("Список предметов:")
    nl = view.PrintList(lesson, True)

    na = ''
    while na == '':
        na = input("Введите оценку: ")
        na = int(na)
    
    assessmant[ns][nl].append(na)

    return assessmant
    
    

    
    

