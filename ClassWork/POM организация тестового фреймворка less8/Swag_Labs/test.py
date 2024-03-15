from Pages.login_page import LoginPage
#from config import driver, base_url
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    base_url = 'https://www.saucedemo.com/'
    # Перейти на указанную страницу
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

import time
# это тест
@pytest.mark.parametrize('username', [('Nastya')])
def test_login_page(driver, username):

    # находим все элементы для заполнения
    login_page = LoginPage(driver) # driver - фикстура

    #  заполняем
    login_page.login(username) # username - параметр передается
    time.sleep(5)
    # проверка на успешную авторизации