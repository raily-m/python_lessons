class Hero:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def __str__(self):
        return f"Герой {self.name}, Здоровье: {self.health}"
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value <= 0:
            self. _health = 0
        else:
            self.__health = value

    @property
    def is_alive(self):
        return self.__health >0


    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось {self.__health} здоровья.")

    def __eq__ (self, other):
         if isinstance (other, Hero):
             return self.health == other.health
         else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance (other, Hero):
             return self.health < other.health
        else:
            return NotImplemented

    def __gt__(self, other):
       if isinstance (other, Hero):
             return self.health > other.health
       else:
            return NotImplemented


hero1 = Hero("Sailor Moon", 100)
print(hero1)
hero1.take_damage(25)
print(hero1)

hero2 = Hero("Sailor Jupiter", 120)
print(hero2)
print (f"Жив ли {hero2.name}? {hero2.is_alive}")

hero2.health = 50
print(hero2)

print(f"Жив ли {hero2.name}? {hero2.is_alive}")


hero3 = Hero("Sailor Mars, 100")
print(hero1 == hero2)
print(hero1 == hero3)
print(hero1 < hero2)
print(hero1 > hero2)
