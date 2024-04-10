# locators.py - содержит локаторы на всех страницах сайта Swag_Labs
from selenium.webdriver.common.by import By

# локаторы авторизации
username = (By.ID, 'user-name')# {'type': By.ID, 'value': 'user-name'}
password = (By.ID, 'password')
button_login = (By.ID, 'login-button')
# локаторы списка товаров
# и т.д.
