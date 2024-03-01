from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Инициализация драйвера (вам нужно подставить свой путь к драйверу)
driver = webdriver.Chrome()

driver.get("file:///C:/Users/marty/PycharmProjects/OAT/ClassWork/OAT%20Xpath-CSS-selector/DOM.html")

try:
    # Использование CSS-селектора для поиска кнопки
    button = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(4) > div > button")#"body div button")


    # Печать сообщения о том, что элемент был найден
    print("Элемент найден:", button.text)

    # Нажатие на кнопку
    button.click()
    first_element_of_list = driver.find_element(By.CSS_SELECTOR, "#myList > li:nth-child(1)")
    print("Элемент найден:", first_element_of_list.text)
except NoSuchElementException:
    # Обработка исключения, если элемент не найден
    print("Элемент не найден")

finally:
    driver.quit()

