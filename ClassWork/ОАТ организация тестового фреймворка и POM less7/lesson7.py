# import time
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# url = "https://runa-land.ru/"
# driver.get(url)
#
# driver.implicitly_wait(5)
# css_locator = '#form1 > div.tpl-field.type-select.field-required.type.select-data1 > div.field-value > div > span.selected'
# property_values = driver.find_element(By.CSS_SELECTOR, css_locator)
#
# driver.execute_script("ele=arguments[0]; ele.innerHTML = 'my new content';", property_values);
# time.sleep(5)


# --------------------------------------------------------------------------------#
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.python.org/search/")
    driver.implicitly_wait(5)
    yield driver


@pytest.mark.parametrize("input_value, expected", [('math', True), ('fadsDsad', "No results found.")])
def test_search(driver, input_value, expected):
    xpath_locator = '//*[@id="content"]/div/section/form/p/input[1]'
    class_loctor = 'list-recent-events.menu'

    input_elem = driver.find_element(By.XPATH, xpath_locator)
    input_elem.click()
    input_elem.send_keys(input_value)  # @pytest.mark.parametrize
    input_elem.send_keys(Keys.ENTER)
    results = driver.find_element(By.CLASS_NAME, class_loctor)
    try:
        results_li = driver.find_elements(By.CSS_SELECTOR, '.' + class_loctor + ' li')  # '.list-recent-events menu li'
        assert expected  # @pytest.mark.parametrize
    except NoSuchElementException:
        results_p = driver.find_element(By.CSS_SELECTOR, '.' + class_loctor + 'p')
        assert results_p.text == expected  # @pytest.mark.parametrize


def test_empty_search(driver):
    xpath_locator = '//*[@id="content"]/div/section/form/p/input[1]'
    class_loctor = 'list-recent-events.menu'

    input_elem = driver.find_element(By.XPATH, xpath_locator)
    input_elem.click()
    input_elem.send_keys('')
    input_elem.send_keys(Keys.ENTER)
    with pytest.raises(NoSuchElementException):  # я ожидаю получение исключения 'NoSuchElementException'
        driver.find_element(By.CLASS_NAME, class_loctor)  # passed test, если исключения сработало


# failed test если исключения не сработало


def test_division_by_zero():
    num = 5
    div = 0
    with pytest.raises(ZeroDivisionError):
        num / div


@pytest.mark.parametrize("input_value, expected", [('math', True), ('fadsDsad', "No results found.")])
def test_case_search(driver, input_value, expected):
    class_locator = 'list-r ecent-events.menu'
    search = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/p/input[1]')
    search.click()
    search.send_keys(input_value)
    search_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/p/input[2]')
    search_button.click()
    results = driver.find_element(By.CLASS_NAME, class_locator)
    try:
        results_li = driver.find_elements(By.CSS_SELECTOR, '#content > div > section > form > ul > li')
        print('\n кол-во найденых элементов', len(results_li))
        assert expected
    except NoSuchElementException:
        results_p = driver.find_element(By.CSS_SELECTOR, '.' + class_locator + ' p')
        assert results_p.text == expected
    time.sleep(2)
