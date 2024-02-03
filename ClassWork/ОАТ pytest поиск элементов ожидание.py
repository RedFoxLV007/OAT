#----------------------------------------------------------------------------------------#
# ГЛОБАЛЬНАЯ ИДЕЯ.
# Пишем тест-кейс (указываем ожидание)
# реализуем получение фактического результата
# должен совпадать ожидание и фактического результата


# https://www.omdbapi.com/?apikey=23f82659&s=matrix

# parametrs
# apikey=23f82659
# s=matrix -  поиск по наименования

# valid values for @param s
# latin
# nums
# specific symbols: spaces - ' "
# minimal count symbols: 3


# example: matrix
# expected result:
# status code 2XX
# response.json()['Response'] == 'True'

# invalid
# example: m
# expected result:
# status code 2XX
# response.json()['Response'] == 'False'

# invalid apikey
# expected result:
# status code 4XX
# response.json()['Response'] == 'False'


# ----------------------------------------------------------------------------# ------------------------ test-case valid params -----------------------#
# import requests
# import pytest
# def test_search_valid_movie():
#     # base_url
#     base_url = "https://www.omdbapi.com/"
#
#     # params
#     api_key = "23f82659"
#     s = "matrix"
#
#     # url
#     url = f"{base_url}?apikey={api_key}&s={s}"
#
#     # send request
#     response = requests.get(url)
#
#     # фактического результат
#     status_code, response_result = response.status_code, response.json()['Response']
#
#     # expected result
#     expected_status_code = range(200, 400)
#     expected_response_result = "True"
#
#     # проверка совпадения наших ожиданий и фактического результат
#     assert (status_code in expected_status_code) and response_result == expected_response_result
#
#
# # ------------------------ test-case invalid param @s -----------------------#
# def test_invalid_search():
#     base_url = "https://www.omdbapi.com/"
#     apikey = "23f82659"
#     s = "m"
#     url = f"{base_url}?apikey={apikey}&s={s}"
#     response = requests.get(url)
#     assert response.status_code in range(200, 300)
#     assert response.json()['Response'] == "False"
#
# # ------------------------ test-case invalid param @apikey -----------------------#
# def test_invalid_apikey():
#     base_url = "https://www.omdbapi.com/"
#     apikey = "rrrr"
#     s = "matrix"
#     url = f"{base_url}?apikey={apikey}&s={s}"
#     response = requests.get(url)
#     assert response.status_code in range(400, 500)
#     assert response.json()['Response'] == "False"



#
#
# # ------------------------ test-case valid params -----------------------#
# import requests
# import pytest
#
# # params
# apikey = "23f82659"
# s = "matrix"
#
# base_url = "https://www.omdbapi.com/"
#
# @pytest.fixture() # эти настройки передавать в каждый тест
# def get_url():#apikey = "23f82659", s = "matrix", base_url = "https://www.omdbapi.com/"):
#     url = f"{base_url}?apikey={apikey}&s={s}"
#     return url
#
#
# def test_search_valid_movie(get_url): # get_url - воспринимает как аргумент тестовой функции
#
#     # send request
#     response = requests.get(get_url)
#
#     # фактического результат
#     status_code, response_result = response.status_code, response.json()['Response']
#
#     # expected result
#     expected_status_code = range(200, 400)
#     expected_response_result = "True"
#
#     # проверка совпадения наших ожиданий и фактического результат
#     assert (status_code in expected_status_code) and response_result == expected_response_result
#
#
# # ------------------------ test-case invalid param @s -----------------------#
# def test_invalid_search(get_url):
#     s = "m"
#     url = f"{base_url}?apikey={apikey}&s={s}"
#     response = requests.get(url)
#     assert response.status_code in range(200, 300)
#     assert response.json()['Response'] == "False"
#
# # ------------------------ test-case invalid param @apikey -----------------------#
# def test_invalid_apikey(get_url):
#     apikey = "rrrr"
#     url = f"{base_url}?apikey={apikey}&s={s}"
#     response = requests.get(url)
#     assert response.status_code in range(400, 500)
#     assert response.json()['Response'] == "False"
#



# #-------------------------------#
# # base_url
# base_url = "https://www.omdbapi.com/"
#
# # params
# api_key = "23f82659"
# s = "matrix"
#
# # url
# url = f"{base_url}?apikey={api_key}&s={s}"
#
# # send requests
# response = requests.get(url)
# print(response, response.status_code, response.json()['Response'])




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import time

@pytest.fixture
def driver():
    # -------------выполняется перед каждым тестом--------------#
    driver = webdriver.Chrome()
    # Перейти на указанную страницу
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount")
    driver.implicitly_wait(5)
    driver.maximize_window()

    #-------------------------точка выхода из подготовки в Тест------------------------------#
    yield driver #
    # -------------выполняется после каждого теста--------------#
    driver.quit()


def test(driver):
    # Найти элемент листбокса "Customer" по XPath
    customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))

    # Выбрать опцию "Harry Potter" # аналог element.click()
    customer_dropdown.select_by_visible_text("Harry Potter")

    # Дополнительная проверка, что выбранное значение отображается корректно
    selected_customer = customer_dropdown.first_selected_option.text
    assert selected_customer == "Harry Potter" # опционально
    driver.save_screenshot(f'customer_name_{selected_customer}.png')



def test_select_currency(driver):
    # Найти элемент листбокса "Customer" по XPath
    customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))
    # Выбрать опцию "Harry Potter" # аналог element.click()
    customer_dropdown.select_by_visible_text("Harry Potter")

    currency_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="currency"]'))
    currency_dropdown.select_by_visible_text("Dollar")

    # Дополнительная проверка, что выбранное значение отображается корректно
    selected_customer = customer_dropdown.first_selected_option.text
    assert selected_customer == "Harry Potter"

    selected_currency = currency_dropdown.first_selected_option.text
    assert selected_currency == "Dollar"
    driver.save_screenshot(f'customer_name_{selected_customer}/currency_{selected_currency}.png')

    button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
    button.click()