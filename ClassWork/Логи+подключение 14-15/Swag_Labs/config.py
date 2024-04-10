# config.py - содержит все необходимые настройки для тестирования
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from pages.login_page import *

import pytest


# Настройка опций для headless режима
chrome_options = Options()
chrome_options.add_argument("--headless")

# Инициализация WebDriver с указанием опций
driver = webdriver.Chrome(options=chrome_options)
base_url = 'https://www.saucedemo.com/'

# хранит адреса страниц
# перенаправляться на эти страницы
# и т.д.
@pytest.fixture(scope="function")

def browser():# надо переимновать
    # Перейти на указанную страницу
    driver.get(base_url)
    print(f"была открыта ссылка {base_url}")
    driver.implicitly_wait(5)
    yield driver