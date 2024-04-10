#Здесь . означает текущий пакет.
from .locators import * # .locatros - переимновала и поставила точку
from .User import *

class LoginPage:
    '''
    __init__ - нужен для опредления элементов на страницы,
    с которыми пользователь может взаимодействовать (поля для ввода, кнопки и т.д.)
    '''
    def __init__(self, driver): # атрибуты страницы
        # Чтобы определить атрибуты страницы, найдем все поля,
        # кнопки и т.д. на страницы

        self.username = driver.find_element(*username)#*username - распаковка данных -> username[0], username[1] #username['type'], username['value']) # атрибут поля username - find_element(username) username из locators.py
        self.password = driver.find_element(password[0], password[1]) # password[0], password[1] = *password атрибут поля password
        self.button_login = driver.find_element(*button_login)# атрибут кнопка

    # методы страницы
    '''
    login - тестовый сценарий
    @param username - тестовое значение имя пользователя
    @param password - тестовое значение пароль
    '''
    def login(self, username: str = '', password: str = ''): #авторизация или вход на страницу
        self.username.send_keys(username)# заполнение поля username
        self.password.send_keys(password)# заполнение поля password
        self.button_login.click()# нажатие на кнопку login



