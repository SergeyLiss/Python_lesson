from telebot import *
from telebot import types
import text
from random import randint as rand

sweets = [f'{(i+1)}' for i in range(text.temp_2)]

botCG = TeleBot(text.TOKEN)

@botCG.message_handler(commands=['start'])
def Start(message):
    botCG.send_message(message.chat.id, text.part_1)
    pass

@botCG.message_handler(commands=['help'])
def Help(message):
    botCG.send_message(message.chat.id, text.part_2)
    pass

@botCG.message_handler(commands=['level'])
def Level(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    markup.add(*text.choice_level)
    botCG.send_message(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)
    pass

def GamePlay(message):
    botCG.send_message(message.chat.id, f"На столе {text.temp_3} конфет\nВаш ход:")

def BotStep(message):
    if text.level_flag:
        number = text.temp_3
        if number > text.temp_2:
            number -= 1
            number %= text.temp_2
            if number == 0:
                number += 1
    else:
        maximum = text.temp_2 if text.temp_2 < text.temp_3 else text.temp_3
        number = rand(1, maximum)
    Steps(message, number, False)
    pass

def ControlWin(message, flag):
    if text.temp_3 == 0:
        me = 'Вы победили' if flag else 'Я победил'
        botCG.send_message(message.chat.id, f'{me}\nМожете начать сначала ->\n/newgame')
    else:
        if flag:
            BotStep(message)
        else:
            GamePlay(message)
    pass

def Steps(message, step, flag):
    text.temp_3 -= step
    me = 'Вы взяли' if flag else 'Я взял'
    botCG.send_message(message.chat.id, f"{me} {step} конфет")
    ControlWin(message, flag)
    pass    

@botCG.message_handler(commands = ["newgame"])
def NewGame(message):
    text.temp_3 = text.temp_1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=4)
    markup.add(*sweets)
    botCG.send_message(message.chat.id, "Новая игра", reply_markup=markup)
    GamePlay(message)
    pass

@botCG.message_handler(content_types = "text")
def Controller(message):
    if message.text in sweets:
        Steps(message, int(message.text), True)
    elif message.text in text.choice_level:
        text.level_flag = True if message.text == text.choice_level[1] else False
        NewGame(message)
    else:
        botCG.send_message(message.chat.id, f"Только цифры от 1 до {text.temp_2}")
    pass

botCG.infinity_polling()