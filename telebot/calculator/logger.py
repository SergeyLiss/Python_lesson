#
from datetime import datetime

class L():
    def __init__(self) -> None:
        self.flag = False
        self.place = ''
        pass

    def __call__(self):
        with open('python/telebot/calculator/log_file_telebot_calc.txt', 'a', encoding='utf-8') as file:
            now_date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
            file.write(f"{now_date}\t{self.place}\n")
            file.close()