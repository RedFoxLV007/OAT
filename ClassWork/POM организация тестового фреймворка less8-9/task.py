#—------------------------------- Задача —--------------------------------#
# Разработайте класс для отслеживания задач в проекте, хранящий информацию о статусе,
# исполнителе, сроках выполнения

class Task:
    def __init__(self,author:str,expair:str,status:str='active'): # expair - srok vipolneniya
        if is_date(expair)== False:
            raise Exception('дата должна быть в формате %d-%m-%Y') # raise - вызов исключения,прирывает работу программы
        self.author = author
        self.expair = expair # проверка является ли датой ?
        self.status = status

    #магический метод - перегрузки оператор
    def __repr__(self): # метод для отоюражения атрибутов класса
        return f'author:{self.author},expair:{ self.expair},status:{self.status}'


    # через show
    def show_info(self):
        return f'author:{self.author},expair:{self.expair},status:{self.status}'

#===============================================================================================================

from datetime import datetime # является ли датой

# вынесли is_date за пределы класса, потому, что в будущем будут добавлены еще классы,
# в которых потребуется такая проверка
def is_date(date):
    # initializing string
    # test_str = '04-01-1997'

    # initializing format
    format = "%d-%m-%Y"

    # checking if format matches the date
    res = True

    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(date, format))
    except ValueError:
        res = False

    return res