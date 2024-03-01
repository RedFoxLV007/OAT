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

def test_search(driver):
    try:
        input_elem = driver.find_element(By.NAME, "q")
        input_elem.click()
        input_elem.send_keys("while")
        input_elem.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("Элемент не найден")
    time.sleep(5)



#=============================================================================================================

def test_case_search(driver):
    search = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/p/input[1]')
    search.click()
    search.send_keys('asdads')
    time.sleep(5)
    search_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/p/input[2]')
    search_button.click()

# =============================================================================================================