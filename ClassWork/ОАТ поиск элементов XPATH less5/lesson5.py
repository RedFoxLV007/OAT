import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://calcus.ru/kalkulyator-ipoteki")
driver.execute_script("document.body.style.zoom='30%'")

driver.implicitly_wait(5)

property_values = driver.find_element(By.NAME, "cost")

submit_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[12]/div/input")

driver.execute_script("arguments[0].click();", submit_button)

time.sleep(5)