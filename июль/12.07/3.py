#Создать класс Book
#Класс должен содержать 3 атрибута name, authot, year
# Фотмат текста - "Буратино", Алексей Толстой Николаевич, 1899г.


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year



    def __str__(self):
        return f"Название книги '{self.name}', автор {self.author}, год {self.year}"

kniga = Book("Буратино", "Алексей Николаевич Толстой", "1989")


print(kniga.name)
print(kniga)