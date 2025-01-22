from TaskManager import TaskManager
from FileManager import FileManager

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
        exitVal = False
        while(not exitVal):
            command = input("Input command:")
            match command:
                case "addTask":
                    name = input("Name of the task:")
                    self.taskManager.addTask(name)
                case "removeTask":
                    name = input("Name of the task:")
                    self.taskManager.removeTask(name)
                case "show":
                    self.taskManager.printList()
                case "checkTask":
                    name = input("Name of the task:")
                    self.taskManager.checkTask(name)
                case "removeChecked":
                    self.taskManager.removeChecked()
                case "reset":
                    self.taskManager.reset()
                case "help":
                    print("Comands:\n1.addTask\n2.removeTask\n3.show\n4.checkTask\n5.removeChecked\n6.reset\n7.help\n8.exit")
                case "exit":
                    self.fileManager.saveList(self.taskManager.list)
                    exitVal = True
                case _:
                    print("Command not found")
'''
prog = GUI()
prog.runLoop()
'''