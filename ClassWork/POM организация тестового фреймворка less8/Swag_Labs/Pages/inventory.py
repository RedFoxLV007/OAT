#Здесь . означает текущий пакет.
from .Locators import *# .locatros - переимновала и поставила точку

class Item:
    def __init__(self): # найти товар по локатору
        self.title = '' # записать наименование товара
        self.price = 0 # записать стоимость товара
        self.btn = ''# запомнить кнопку

    def btn_click(self):
        pass # меняется название действия кнопки # и нажатие на кнопку

class InventoryPage:
    def __init__(self, driver):
       # self.list_items = ['item_obj'] # а нужно ли ?
        self.btn_sort = '' # ищем элемент, который сортировку

    def add_to_cart(self, item): #добавление товаров в корзину
       pass

    def sort_items(self):# сортировка товаров на странице
        pass
