from TaskManager import TaskManager
from FileManager import FileManager
import os

class GUI:

    def __init__(self):
        self.fileManager = FileManager()
        self.taskManager = TaskManager(self.fileManager.loadList())
        print(" _____      ______        _     _     _   ")
        print("|_   _|     |  _  \      | |   (_)   | |  ")
        print("  | | ___   | | | |___   | |    _ ___| |_ ")
        print("  | |/ _ \  | | | / _ \  | |   | / __| __|")
        print("  | | (_) | | |/ / (_) | | |___| \__ \ |_")
        print("  \_/\___/  |___/ \___/  \_____/_|___/\__|")
        self.taskManager.printList()
        print("Type help to check commands")

    def runLoop(self):
        title = "Python Script Notification"
        message = "Hello from Termux!"
        os.system(f'termux-notification --title "{title}" --content "{message}"')
        exitVal = False
        changes = 0
        while(not exitVal):
            command = input("Input command:")
            match command:
                case "addTask":
                    name = input("Name of the task:")
                    if self.taskManager.addTask(name):
                        changes = changes+1
                case "removeTask":
                    name = input("Name of the task:")
                    if self.taskManager.removeTask(name):
                        changes = changes+1
                case "show":
                    self.taskManager.printList()
                case "checkTask":
                    name = input("Name of the task:")
                    if self.taskManager.checkTask(name):
                        changes = changes+1
                case "removeChecked":
                    changes = changes + self.taskManager.removeChecked()
                case "reset":
                    loopBreaker = False
                    while loopBreaker==False:
                        confirmation = input("Are you sure (y/n):")
                        if confirmation == "y":
                            changes = changes + self.taskManager.reset()
                            loopBreaker = True
                        elif confirmation == "n":
                            loopBreaker = True
                            print("List not deleted")
                        else:
                            print("Invalid input")
                case "save":
                    self.fileManager.saveList(self.taskManager.list)
                    print(str(changes)+" saved correctly")
                    changes = 0
                case "help":
                    print("Comands:\n1.addTask\n2.removeTask\n3.show\n4.checkTask\n5.removeChecked\n6.reset\n7.save\n8.help\n9.exit")
                case "exit":
                    if changes > 0:
                        loopBreaker = False
                        while loopBreaker == False:
                            saveChanges = input("There are " + str(changes) + " unsaved changes, would you like save them?(y/n):")
                            if saveChanges == "y":
                                self.fileManager.saveList(self.taskManager.list)
                                print(str(changes) + " saved correctly")
                                changes = 0
                                loopBreaker = True
                                exitVal = True
                            elif saveChanges == "n":
                                loopBreaker = True
                                print(str(changes)+" not saved")
                                exitVal = True
                            else:
                                print("Invalid input")
                    else:
                        exitVal = True
                case _:
                    print("Command not found")
        return exitVal

    def notify(self):
        notification.notify(
            title="Alerta",
            message="Esto es una notificación desde Python en Termux",
            app_name="Termux"
        )
'''
prog = GUI()
prog.runLoop()
'''