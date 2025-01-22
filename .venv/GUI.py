from TaskManager import TaskManager
from FileManager import FileManager

class GUI:

    def __init__(self):
        self.fileManager = FileManager()
        self.taskManager = TaskManager(self.fileManager.loadList())
        print("Evoblast To Do List")
        self.taskManager.printList()
        print("Type Help to check commands")

    def runLoop(self):
        exitVal = False
        while(not exitVal):
            command = input("Input command:")
            match command:
                case "AddTask":
                    name = input("Name of the task:")
                    self.taskManager.addTask(name)
                case "RemoveTask":
                    name = input("Name of the task:")
                    self.taskManager.removeTask(name)
                case "PrintList":
                    self.taskManager.printList()
                case "CheckTask":
                    name = input("Name of the task:")
                    self.taskManager.checkTask(name)
                case "RemoveChecked":
                    self.taskManager.removeChecked()
                case "Reset":
                    self.taskManager.reset()
                case "Help":
                    print("Comands:\n1.AddTask\n2.RemoveTask\n3.PrintList\n4.CheckTask\n5.RemoveChecked\n6.Reset\n7.Help\n8.Exit")
                case "Exit":
                    self.fileManager.saveList(self.taskManager.list)
                    exitVal = True
                case _:
                    print("Command not found")
'''
prog = GUI()
prog.runLoop()
'''