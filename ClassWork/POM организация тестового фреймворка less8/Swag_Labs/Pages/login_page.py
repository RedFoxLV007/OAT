#import Locators
from selenium.webdriver.common.by import By

class LoginPage:
    '''
    __init__ - нужен для опредления элементов на страницы,
    с которыми пользователь может взаимодействовать (поля для ввода, кнопки и т.д.)
    '''
    def __init__(self, driver): # атрибуты страницы
        # Чтобы определить атрибуты страницы, найдем все поля,
        # кнопки и т.д. на страницы

        self.username = driver.find_element(By.ID, 'user-name') # атрибут поля username - find_element(username) username из Locators.py
        # атрибут поля password
        self.password = driver.find_element(By.ID, 'password')
        # атрибут кнопка
        self.button = driver.find_element(By.ID, 'login-button')





    # методы страницы
    '''
    login - тестовый сценарий
    @param username - тестовое значение имя пользователя
    @param password - тестовое значение пароль
    '''
    def login(self, username: str = '', password: str = ''): #авторизация или вход на страницу
        self.username.send_keys(username)# заполнение поля username
        # заполнение поля password
        self.password.send_keys(password)
        # нажатие на кнопку login
        self.button.click()
