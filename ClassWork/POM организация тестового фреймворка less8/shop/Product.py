#-----------------------Задача 2 -----------------------------#
# Создайте класс, представляющий продукт  в магазине, хранящий информацию
# о его названии,
# цене, количестве на складе и категории
# и добавьте методы просмотр товара, скидка (размер скидки)

class Product:
    def __init__(self, name, price: int, count: int, category):
        self.name = name
        self.price = price
        self.count = count
        self.category = category

    def __repr__(self):
        return f"name: {self.name}\nprice: {self.price}\ncount: {self.count}\ncategory: {self.category}\n"

    def discount(self, procent):
        if not (type(procent) in [int,float]) and procent <= 0:
            raise Exception('Процент должен быть числом большн нуля')
        return self.price * (100 - procent) / 100


tomato = Product("tomato", 200, 4, "vegetable")
print(tomato)
print(tomato.discount(5))