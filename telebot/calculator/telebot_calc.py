from telebot import *
from calculate import *
from logger import *

TOKEN = '5927273583:AAHpJ2C2GTG_Rdcmu19CLbIr-WHofgW3Ef4'
row_line = [4, 5]
# button24 = ['π', 'e', '1/x', '%', 'xⁿ', 'x²', '√x', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', 'i', '0', '.', '=']
# button24 = ['CE', 'C', '1/x', '%', 'xⁿ', 'x²', '√x', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', 'i', '0', '.', '=']
button24 = ['CE', 'xⁿ', '%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', 'i', '0', '.', '=']

operation = TBCalc()
logf = L()
botC = TeleBot(token=TOKEN)
keyboard = types.InlineKeyboardMarkup()
for i in range(row_line[1]):
    keyboard.row(*[types.InlineKeyboardButton(button24[row_line[0]*i+j], callback_data=button24[row_line[0]*i+j]) for j in range(row_line[0])])

@botC.message_handler(commands=['start', 'calculater'])
def FormCalc(message):
    botC.send_message(message.from_user.id, button24[17], reply_markup=keyboard)

@botC.callback_query_handler(func=lambda call: True)
def Controller(query):
    if query.data in operation.operand_list:
        operation.flag = True
        index = 0
        for i in range(len(operation.operand_list)):
            if query.data == operation.operand_list[i]:
                index = i
        if operation.operand == ' ':
            operation.number_1 = operation.number_2
            operation.number_2 = button24[17]
            operation.operand = query.data
        else:
            if operation.compl:
                logf.place = f'{operation.number_1}{operation.operand}{operation.number_2}'
                operation.number_2 = operation()
                logf.place += f'={operation.number_2}\t'
                operation.number_1 = operation.number_2
                operation.operand = query.data
                logf.flag = True
            else:
                operation.number_2 += query.data + 'i'
                operation.compl = True
                operation.flag = False
    elif query.data == 'CE':
        operation.number_1 = ' '
        operation.number_2 = button24[17]
        operation.operand = ' '
        operation.flag = True
    elif query.data == 'i':
        if operation.compl:
            if operation.operand in ['+', '-']:
                operation.number_2 = operation.number_1 + operation.operand + query.data
                operation.number_1 = ' '
                operation.operand = ' '
                operation.compl = False
                operation.flag = False
            else:
                operation.number_2 = 'Не правильное комплексное число.'
                operation.number_1 = ' '
                operation.operand = ' '
                operation.flag = True
    else:
        if operation.flag:
            operation.number_2 = query.data
            operation.flag = False
        else:
            operation.number_2 += query.data
    
    
    if operation.number_2 != operation.otvet:
        operation.otvet = operation.number_2
        botC.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=operation.otvet, reply_markup=keyboard)
        if logf.flag:
            logf.place = f'{query.id} {query.from_user.first_name} {logf.place}'
            logf()
            logf.place = ''
            logf.flag = False 
    
botC.infinity_polling()
