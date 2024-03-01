# with open("тестовые значения.csv", 'r', encoding='utf-8') as f:
#     lines = f.readlines()[1:]
#
# print(lines)
# params = list(map(lambda string: tuple(string.replace('\n','').split(',')),lines))
# print(params)
#['10,10\n', '1,1\n', '0,1\n', '-1,1\n', '5.15,5\n', '"5,95",5']
#[('10', '10'), ('1', '1'), ...]
def get_test_params(filename=''):
    with open("тестовые значения.csv", 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]#не берем первую строку

    #params = list(map(lambda string: tuple(string.replace('\n', '').split(',')), lines[:-1])) # -> [('10', '10'), ('1', '1'), ...]
    print(lines)
    for i,line in enumerate(lines[:-1]):#перебираем все элементы, кроме последнего
        line = line.replace('\n','')
        lines[i] = tuple(line.split(','))
    print(lines)
    last_element = (lines[-1].split('"')[1], lines[-1].split('"')[2][1:])
    #print(lines[-1].split('"'))
    lines[-1] = last_element
    return lines # или params

#print(get_test_params())

import time

import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture()
def driver():
    # -------------выполняется перед каждым тестом--------------#
    driver = webdriver.Chrome()
    # Перейти на указанную страницу
    driver.get("http://shop.bugred.ru/shop/item/9")
    driver.implicitly_wait(5)
    driver.maximize_window()

    # -------------------------точка выхода из подготовки в Тест------------------------------#
    yield driver  #
    # -------------выполняется после каждого теста--------------#
    driver.quit()
# # [(),(),()]
@pytest.mark.parametrize("input_value, expected", get_test_params())
def test_add_item_to_cart(driver, input_value, expected):
    input_elem = driver.find_element(By.ID, "exampleCount")
    input_elem.send_keys(input_value)# input_value взяли из @pytest.mark.parametrize
    button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/button")
    button.click()


    driver.get("http://shop.bugred.ru/shop/cart/index")
    driver.implicitly_wait(5)
    items_count = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/form/table/tbody/tr[1]/td[2]/input").get_attribute("value")
    assert items_count == expected # input_value и expected взяли из @pytest.mark.parametrize
    current_date = datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    name_screenshot = 'screenshots/full_page_screenshot' + current_date + '.png'
    driver.save_screenshot(name_screenshot)


