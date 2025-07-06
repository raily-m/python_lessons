class Person:

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__fullname = name + surname


    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname
    
    def get_fullname(self):
        return self.__fullname
    
    def setname(self, newname):
        self.__name = newname
        self.__fullname = self.__name + self.__surname

    def setname(self, newsurname):
        self.__surname = newsurname
        self.__fullname = self.__name + self.__surname

p = Person("Иван", "Иванов")
print (p.get_fullname())