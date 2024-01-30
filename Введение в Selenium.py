from selenium import webdriver # импорт веб драйвера
from selenium.webdriver.common.by import By # импорт поиска
from selenium.webdriver.common.keys import Keys # импорт клавиш
import time # импорт задержки


driver = webdriver.Chrome()#подключить веб драйвер
driver.maximize_window()#расширить окно
driver.get("https://www.google.com/")#перейти на сайт
elem = driver.find_element(By.NAME,"q")
elem.click()#кликнуть
elem.send_keys("кошка")#написать
elem.send_keys(Keys.ENTER) #нажать кнопку
time.sleep(3) #задержка
driver.save_screenshot("Screen.png")  #скрин
url = driver.current_url # вывести урл
print(url) #вывести
# следующая страница
elem = driver.find_element(By.NAME,"q")
elem.clear()
elem.send_keys("Собака")
elem.send_keys(Keys.ENTER)
time.sleep(3)
driver.back() #назад перейти
time.sleep(3)
driver.forward()#вперед перейти
time.sleep(3)
# закрытие окно
driver.close()
# закрытия браузера
driver.quit()
