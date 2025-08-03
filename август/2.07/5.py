import json

file_name = ''

musicians = {
    'Linkin Park' : ["Reanimation", "Hybrid Theory"],
    'Rammstein': ["Mutter", "Zeit"],
    'Мияги': ["Ямакаси", "Бастер Китон"]
}

def show_menu():
    print("Выберите операцию:")
    print("0 - Загрузить данные из файла")
    print("1 - Выбрать группу")
    print("2 - Добавить группу")
    print("3 - Удалить группу")
    print("4 - Сохранить изменения")
    print("5 - Выход")

while True:
    show_menu()
    choice = int(input())
    if choice == 0:
        file_name = input("Введите название файла для загрузки: \n")
        try:
            with open(file_name, "r", encoding="utf-8") as fl:
                musicians = json.load(fl)
            print(f"Файл с именем {file_name} успешно загружен!")

        except FileNotFoundError:
            answer = input("Файл не найден, создать пустой каталог, (Да/Нет): \n")
            if answer.lower().strip() == 'да':
                with open(file_name, "w", encoding="utf-8") as fl:
                    json.dump(musicians, fl)
                print(f"Файл с именем {file_name} успешно создан!")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


            pass
    elif choice == 1:
        group = input("Введите название группы: ")
        if musicians.get(group, None) is not None:
            print(musicians.get(group, None))
        else:
            print(f"Группы {group} нет в каталоге!")
            
    elif choice == 2:
        group_for_add = input("Введите название группы для добавления: ")
        if musicians.get(group_for_add, None) is not None:
            print(f"Группа {group_for_add} уже есть в каталоге")
        else:
            musicians[group_for_add] = []
            print(f"Группа {group_for_add} добавлена в каталог")
            answer = input("Хотите добавить альбомы к группе? (Да/Нет): ")
            if answer.lower().strip() == 'да':
                albums = input("Введите одно или несколько названий альбомов через запятую: \n")
                if albums.isspace():
                    print("Строка пуста, альбомы не добавленны")
                else:
                    musicians[group_for_add] = [x.strip().capitalize() for x in albums.split(',')]
                    print(f"Для {group_for_add} добавлены альбомы: {musicians[group_for_add]}")
            
    elif choice == 3:
        group_for_del = input("Введите название группы для удаления: ")
        try:
            musicians.pop(group_for_del)
            print(f"Группа {group_for_del} успешно удалена!")
        except:
            print("Такой группы нет в каталоге")


    elif choice == 4:
        if not file_name:
            answer = input("Не выбран файл для сохранения, создать новый файл? (Да/Нет): \n")
            if answer.lower().strip() == 'да':
                file_name = input("Введите название файла для созранения: \n")

            else:
                print("Изменения сохранены!")
                continue
        with open (file_name, "w", encoding = "utf-8") as fl:
            json.dump(musicians, fl)
        print(f"Все изменения сохранены успешно в {file_name}!")


    elif choice == 5:
        print("Ввыходим из программы")
        break
else:
    print("Введена некорректная команда")

input ("Нажмите для продолжения")