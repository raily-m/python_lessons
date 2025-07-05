# класс ГАн
#count - количество выстрелов. В начале равно 0
#метод shoot - при вызове пишет pif
#метод shoots_count - возвращает нам количество выстрелов


class Gun:

    def __init__(self):
        self.count = 0


    def shoot(self):
        print("pif")
        self.count +=1


    def shoot_count(self):
        return self.count
      

my_gun = Gun()
print(my_gun.shoot_count())
my_gun.shoot()
print(my_gun.shoot_count())


  

