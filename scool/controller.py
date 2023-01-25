import generation, interaction, view

test = generation.Generator()

def Deistvie():
    flag = True
    student = [[],[],[]]
    lesson = []
    assessmant = []
    while flag != False:
        print("Выберите действие:")
        for i in view.interface:
            print(i)
        
        ch = input()

        if ch == '0':
            student = test.GenStudent()
            lesson = test.GenTable()
            assessmant = test.GenAssessment(student, lesson)
        elif ch == '1':
            student = interaction.AddStudent(student)
        elif ch == '2':
            print('3333')
            test.lessons_list.append(interaction.AddLesson())
        elif ch == '3':
            assessmant = interaction.AddAssessment(assessmant, student, test.lessons_list)
        elif ch == '4':
            view.PrintClasses(student)
        elif ch == '5':
            view.ListAssessmant(assessmant, student, test.lessons_list)
        elif ch == '6':
            view.MediumAssesmantStudent(assessmant, student, test.lessons_list)
        elif ch == '7':
            view.MediumAssesmantLesson(assessmant, student, test.lessons_list)
        elif ch == '8':
            view.GoldenHonor(assessmant, student, test.lessons_list)
        elif ch == '9':
            assessmant = test.GenAssessment(student, lesson)
        else:
            flag = False
            

