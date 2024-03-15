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

@pytest.mark.parametrize("input_value, expected", [("8", ["8","Ваша корзина пуста!"]), ("999999999999999999999999", ["100","Ваша корзина пуста!"]), ("-100", ["1","Ваша корзина пуста!"])])
def test_add_item_to_cart(driver, input_value, expected):
    input_elem = driver.find_element(By.ID, "exampleCount")
    input_elem.send_keys(input_value)
    time.sleep(5)
    button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/button")
    button.click()
    driver.get("http://shop.bugred.ru/shop/cart/index")
    driver.implicitly_wait(5)
    items_count = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/form/table/tbody/tr[1]/td[2]/input").get_attribute("value")
    assert items_count == expected[0]
    driver.save_screenshot("file.jpg")


    # ------------офрмление заказа------------ #
    phone = driver.find_element(By.ID,"InputPhone")
    phone.send_keys("89375484982")
    address = driver.find_element(By.ID,"InputAddr")
    address.send_keys("г. Москва")
    driver.save_screenshot(f"confirm_order.jpg")
    confirm_btn = driver.find_element(By.XPATH, "/html/body/div/div/form/div/div[3]/button")
    confirm_btn.click()
    # если появится доступ, то допишем проверку по БД (через апи)
    driver.get("http://shop.bugred.ru/shop/cart/index")
    wait = WebDriverWait(driver, timeout=3)
    p = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/p")))
    #div = driver.find_element(By.CLASS_NAME, "alert alert-danger")
    assert p.text == expected[1]




