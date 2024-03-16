import ui
import commadUi
def start():
    while True:
        ui.consoleMenu()
        userInput = input()
        if userInput == '1':
            commadUi.show("all")
        elif userInput == '2':
            commadUi.show("ID")
        elif userInput == '3':
            commadUi.show("date")
        elif userInput == '4':
            commadUi.show("all")
            commadUi.change_note()
        elif userInput == '5':
            commadUi.add_note()
        elif userInput == '6':
            commadUi.show("all")
            commadUi.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break