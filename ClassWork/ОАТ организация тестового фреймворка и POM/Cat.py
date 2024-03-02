class Cat:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
    #действия, которые данный клас может делать
    def eat(self):
        print(f'{self.name} eat')

    def sleep(self):
        print(f'{self.name} sleep')


my_cat = Cat('Felix', 'tiger', 'scottish straight')
freinds_cat = Cat('Vasya', 'black', '')
my_cat.eat()
freinds_cat.sleep()