def consoleMenu():
    printMenuTitle("Главное меню\n           ЖУРНАЛ ЗАМЕТОК")
    print("1 - вывод журнала \n2 - вывод заметки по id \n3 - выбор заметки по дате\n4 - редактирование заметки"
          " \n5 - добавление заметки\n6 - удаление заметки\n7 - выход")
    printMenuLine()
    print("\n введите пункт из меню ")


def printMenuTitle(textMenu):
    print("-----------------------")
    print("            ",textMenu)
    print("-----------------------")

def printMenuLine():
    print("-----------------------")