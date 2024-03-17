

from Pages.login_page import LoginPage
import pytest
from selenium import webdriver
from Pages.User import *


# from config import *

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    base_url = 'https://www.saucedemo.com/'

    # Перейти на указанную страницу
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


import time

@pytest.fixture()
def data_cases():
    data = data_login(test_cases)
    yield data

# это тест
@pytest.mark.parametrize('username ,password,expected_url',  data_login(test_cases))
def test_login_page(browser, username, password, expected_url):
    # находим все элементы для заполнения
    login_page = LoginPage(browser)  # driver - фикстура

    #  заполняем
    login_page.login(username, password)  # username - параметр передается
    time.sleep(5)

    # проверка на успешную авторизации

    #print(browser.current_url, browser.current_url == expected_url)

    #assert browser.current_url == expected_url # =====  не понятно ??????

    # input-data:
    #     # username = 'stabdart_user'
    #     # passord = 'secret_sauce'
    #     # expected: "https://www.saucedemo.com/inventory.html"

    # input-data: locked_out_user
    # username = 'locked_out_user'
    # passord = 'secret_sauce'
    # expected: "https://www.saucedemo.com/"
