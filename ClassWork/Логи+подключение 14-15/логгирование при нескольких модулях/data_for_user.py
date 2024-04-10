import logging

# Настройка логирования
logging.basicConfig(filename='auth.log',  # куда будем сохранить данные
                    encoding='utf-8', # кодировка
                    format='%(asctime)s  | %(levelname)s  |  %(message)s  ', # формат записи
                    level=logging.INFO #  уровень логгирования - важность записи данных в лог
                    )

def make_test_data_login(filename):
    logging.info("data_for_user logs")
    #код, который сделает словарь
    test_data_login = {
        "username": "test",
        "password": "test"
    }
    return test_data_login

def make_test_data_registration(filename):
    # код, который сделает словарь
    test_data_registration = {
        "username": "test",
        "password": "test"
    }
    return test_data_registration
