# Логирование
from datetime import datetime

class Logg():

    def __init__(self, path_log) -> None:
        self.path_log = path_log
        self.text = ''
        pass
    
    def Logger(self):
        # now_date = f"{datetime.now()}"[:19]
        now_date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
        file_log = open(self.path_log, "a", encoding="utf-8")
        file_log.write(f"{now_date}\t{self.text}\n")
        file_log.close()