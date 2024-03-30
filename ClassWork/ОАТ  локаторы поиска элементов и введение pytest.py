from selenium import webdriver # импорт веб драйвера
from selenium.webdriver.common.by import By # импорт поиска
from selenium.webdriver.common.keys import Keys # импорт клавиш
import time
from selenium.common import NoSuchElementException # если не выводить то /except NoSuchElementException:/print('')
from selenium.webdriver.support.wait import WebDriverWait # драйвер ожидания
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0") #страница сайта
# try:
#    elem = driver.find_element(By.ID, "searchInput") #поиск по ID
#    print('Элемент нашелся') #вывод если нашелся
# except NoSuchElementException:  #вывод если нет
#    print(":(") #сам вывод если нет
# driver.close() #закрыть браузер

# ------------By.TAG_NAME-------------#
# try:
#    elements = driver.find_elements(By.TAG_NAME, "p") #поиск элементов Р
#    print(elements, len(elements)) #показать элементы в списке
#    for element in elements: #перебор
#       print(element.text, '\n\n----------------------\n\n') #печатать содержимое перебора с разделеннем ----
# except NoSuchElementException: #если нет
#    print("нет ни одного элемента")



# Парсинг — это автоматизированный сбор и структурирование информации с сайтов при помощи программы или сервиса.
# Эта программа называется парсер и её задачей является сбор информации в соответствии с заданными параметрами.



# --------------------------------ЗАДАНИЕ-------------------------------------- #
# (Откройте любую страницу википедии
# Найдите любую картинку
# Если картинка не найдена, напечатайте “нет найден элемент)


# driver = webdriver.Chrome()
# driver.get("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0")
# try:
   # elem = driver.find_element(By.CLASS_NAME, "mw-file-element") # можно через класс
   # elem = driver.find_element(By.TAG_NAME, "img")# можно через тег фото
#    elem = driver.find_elements(By.TAG_NAME, "img")  # можно через тег фотографии Элементы
#    print(f'{len(elem)} Элемент нашелся') # вывести все фотографии (колличество) на странице
#    print(elem[0].size)# вывести размеры изображение
# except NoSuchElementException:
#    print(":(")
# driver.close()

# ----------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------#
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust")

wait = WebDriverWait(driver, timeout=10)# задержка топ вариант
element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))# задержка топ вариант

# driver.implicitly_wait(5) #загрузилась на 2 секунде, то мы СРАЗУ продолжим исполнять или слип но /вариант 2/

# time.sleep(5)# страница еще не была загружена по этому слип (так делать нельзя) слип тормозит всю программу
form_elements = driver.find_elements(By.TAG_NAME, 'input')
firstName = form_elements[0] # ошибка
lastName = form_elements[1]
postCode = form_elements[2]
testCase = {"firstName": "User1",               # сам текст-кейс
            "lastName": "User1",
            "postCode": "1"} # брать данные из таблиц, текстовых и т.д.
firstName.click() #firstName - объект класс webElement
firstName.send_keys(testCase['firstName'])
lastName.click()
lastName.send_keys(testCase['lastName'])
postCode.click()
postCode.send_keys(testCase['postCode'])
driver.save_screenshot(f'{testCase["firstName"]}.png')# скрин


# ===============    DOM =======================

# это объектная модель документа, которую браузер создает в памяти компьютера на основании HTML-кода,
# полученного им от сервера.
# Иными словами, это представление HTML-документа в виде дерева тегов.

# def see_page():
#     print("see page")
# def add_products_to_card(product):
#     print(f'{product} add to card')
#
# client = {"name": 'client1', 'age': 25, 'actions': [see_page()]}


class Cat:
    def __init__(self, name, age): # инциализатор - запись характеристик
        self.name = name #self.name -> поле == свойство == атрибут  \характеристика!
        self.age = age #self.age -> поле == свойство == атрибут  \характеристика!

my_cat = Cat(name="Barsik", age=2) # my_cat -> объект == экзмепляр класс Cat1
print(f"name: {my_cat.name}, age: {my_cat.age}")

friend_cat = Cat(name="Vasya", age=5) # friend_cat -> объект == экзмепляр класс Cat2
print(f"name: {friend_cat.name}, age: {friend_cat.age}")


# Классы в Python =  определяются с помощью ключевого слова class и имени класса, за которым следует двоеточие.
# Внутри класса могут быть определены атрибуты и методы.


class MyClass:
    attribute = "Some value"

    def my_method(self):
        print("Hello from my_method")


# В примере выше создан
# класс MyClass с атрибутом attribute и методом
# my_method.

