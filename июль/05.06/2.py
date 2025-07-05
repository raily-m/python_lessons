#Создать класс Дом
#Две характеристики 1 - количестов комнат 2 - цвет дома
#Действя
# 1 - Покрасить дом в новый цвет
# 2 - Добавить комнату

class House:
    def __init__(self, count, color):
        self.count = count
        self.color = color

    def paint_house (self, new_color):
        self.color = new_color
        print (f"Дом покрашен в {self.color} цвет")

    def add_room (self):
        self.count +=1
        print (f"В доме {self.count} комнат")


my_house = House (4, "зеленый")
my_house.paint_house ("синий")
my_house.add_room ()
print (my_house.paint_house)
print (my_house.add_room)



    