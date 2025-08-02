musicians = {
    'Linkin Park' : ["Reanimation", "Hybrid Theory"],
    'Rammstein': ["Mutter", "Zeit"],
    'Мияги': ["Ямакаси", "Бастер Китон"]
}

def show_menu():
    print("Выберите операцию:")
    print("1 - Выбрать группу")
    print("2 - Добавить группу")
    print("3 - Удалить группу")
    print("3 - Выход")

while True:
    show_menu()
    choice = int(input())
    if choice == 1:
        group = input("Введите название группы: ")
        if musicians.get("group_for_add", None) is not None:
            print(musicians.get("group_for_add", None))
        else:
            print(f"Группы {group_for_add} нет в каталоге!")
            
    elif choice == 2:
        group_for_add = input("Введите название группы для добавления: ")
        if musicians.get("group_for_add", None) is not None:
            print(f"Группа {group_for_add} уже есть в каталоге")
        else:
            musicians[group_for_add] = []
            print(f"Группа {group_for_add} добавлена в каталог")
    elif choice == 3:
        group_for_del = input("Введите название группы для удаления: ")
        try:
            musicians.pop(group_for_del)
            print(f"Группа {group_for_del} успешно удалена!")
        except:
            print("Такой группы нет в каталоге")
    elif choice == 4:
        print("Ввыходим из программы")
        break
else:
    print("Введена некорректная команда")

input ("Нажмите для продолжения")