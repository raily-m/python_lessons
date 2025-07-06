from math import pi


class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diametr = 2*radius
        self.__area = pi * radius **2


    def get_radius(self):
        return self.__radius
        
    def get_diametr(self):
        return self.__diametr
        
    def get_area(self):
        return self.__area
    
    def set_radius (self, new_radius):

        
c1 = Circle(1)
print(f"Радиус круга равен {c1.get_radius()}\nДиаметр равен {c1.get_diametr()}\nПлощадь круга равна {c1.get_area()}")
print ("Изменим радиус")
с1.set_radius(3)
print(f"Радиус круга равен {c1.get_radius()}\nДиаметр равен {c1.get_diametr()}\n")
