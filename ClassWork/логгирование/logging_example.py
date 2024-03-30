'''

наша программа


функция регистрации пользователя:
    Взяли данные от пользователя
    обращаемся к БД
    получаем ответ (успешно или нет)


сделай запись в лог("начало регистрации")  #print("начало регистрации")
обращаемся к функции регистрации пользователя
сделай запись в лог("конец регистрации")
'''

import logging

# Настройка логирования
logging.basicConfig(filename='example.log',  # куда будем сохранить данные
                    encoding='utf-8', # кодировка
                    format='%(asctime)s  | %(levelname)s  |  %(message)s  ', # формат записи
                    level=logging.ERROR #  уровень логгирования - важность записи данных в лог
                    )

# Деление на ноль
def divide(x, y):
    try:
        result = x / y # Основной код
    except ZeroDivisionError:
        #print("Попытка деления на ноль")
        logging.error("Попытка деления на ноль")
        logging.debug("что-то для примера debug")
        logging.warning("что-то для примера warning")
        logging.fatal("что-то для примера fatal")
    except:
        #print("Какая-то иная ошибка")
        logging.error("Какая-то иная ошибка")
    else:
        #print(f"Результат деления: {result}")
        logging.info(f"Результат : {result}")

logging.fatal("-----------level:error---------------")
divide(10, 2)  # Запись информации о результате деления
divide(10, 0)  # Запись сообщения об ошибке деления на ноль

