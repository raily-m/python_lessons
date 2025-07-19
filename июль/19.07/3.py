class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("Zzzzz")

class Cat(Animal):
    def say(self):
        print("Mяу")


class Dog(Animal):
    def say(self):
        print("Гав")

_animal = Animal("Животное", 10)
_cat = Cat("Леопольд", 45)
_dog = Dog("Шарик", 12)


print(_animal.name)
print(_cat.name)

_animal.sleep()
_cat.sleep()
_cat.say()
_dog.say()