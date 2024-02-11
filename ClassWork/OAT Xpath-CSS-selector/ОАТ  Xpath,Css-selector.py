
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Инициализация драйвера (вам нужно подставить свой путь к драйверу)
driver = webdriver.Chrome()

driver.get("file:///C:/Users/marty/PycharmProjects/OAT/ClassWork/OAT%20Xpath-CSS-selector/DOM.html")

try:
# Использование CSS-селектора для поиска кнопки
    button = driver.find_element(By.CSS_SELECTOR,"#myButton")#"body div button")


# Печать сообщения о том, что элемент был найден
    print("Элемент найден:", button.text)

# Нажатие на кнопку
    button.click()

except NoSuchElementException:
    # Обработка исключения, если элемент не найден
    print("Элемент не найден")

# finally:
# driver.quit()
#
#
# elements = driver.find_elements_by_css_selector("button#myButton.btn")
#
# if len(elements) > 0:
#     print("Элемент найден:", elements[0].text)
#     elements[0].click()
# else:
#     print("Элемент не найден")
#
# button = driver.find_element_by_css_selector("button#myButton.btn")
#
# if button.is_displayed():
#     print("Элемент найден:", button.text)
#     button.click()
# else:
#     print("Элемент не найден")
#
#
# button = driver.find_element_by_css_selector("button#myButton.btn")
#
# if button.is_enabled():
#     print("Элемент найден:", button.text)
#     button.click()
# else:
#     print("Элемент не найден")

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
        lines = f.readlines()[1:]

    params = list(map(lambda string: tuple(string.replace('\n', '').split(',')), lines[:-1])) # -> [('10', '10'), ('1', '1'), ...]
    last_element = (lines[-1].split('"')[1], lines[-1].split('"')[2][1:])
    #print(lines[-1].split('"'))
    params.append(last_element)
    return params
    # print(params)
#print(get_test_params())
import time

import pytest
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
    driver.save_screenshot("file.jpg")