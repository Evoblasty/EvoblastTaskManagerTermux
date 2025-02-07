from Command.CommandInterface import CommandInterface
from IOManager import IOManager

class addTask(CommandInterface):
    def __init__(self,taskManager):
        self.taskManager = taskManager

    def apply(self):
        ioManager = IOManager()
        name = ioManager.readInput("Name of the task:")
        if name:
            return self.taskManager.addTask(name)
        else:
            print("Error adding task")
            return 0

class removeTask(CommandInterface):
    def __init__(self,taskManager):
        self.taskManager = taskManager

    def apply(self):
        ioManager = IOManager()
        name = ioManager.readInput("Name of the task:")
        if name:
            return self.taskManager.removeTask(name)
        else:
            print("Error deleting task")
            return 0

class show(CommandInterface):
    def __init__(self, taskManager):
        self.taskManager = taskManager

    def apply(self):
        self.taskManager.printList()
        return 0


class checkTask(CommandInterface):
    def __init__(self, taskManager):
        self.taskManager = taskManager

    def apply(self):
        ioManager = IOManager()
        name = ioManager.readInput("Name of the task:")
        if name:
            return self.taskManager.checkTask(name)
        else:
            print("Error checking task")
            return 0


class saveTasker(CommandInterface):
    def __init__(self,taskManager,FileManager):
        self.taskManager = taskManager
        self.fileManager = FileManager

    def apply(self):
        self.fileManager.saveList(self.taskManager.list)
        print("Changes saved correctly")
        return 0

class loadTasker(CommandInterface):
    def __init__(self,taskManager):
        self.taskManager = taskManager

    def apply(self):
        print(" _____      ______        _     _     _   ")
        print("|_   _|     |  _  \      | |   (_)   | |  ")
        print("  | | ___   | | | |___   | |    _ ___| |_ ")
        print("  | |/ _ \  | | | / _ \  | |   | / __| __|")
        print("  | | (_) | | |/ / (_) | | |___| \__ \ |_")
        print("  \_/\___/  |___/ \___/  \_____/_|___/\__|")
        self.taskManager.printList()
        print("Type help to check commands")


class removeChecked(CommandInterface):
    def __init__(self, taskManager):
        self.taskManager = taskManager

    def apply(self):
        return self.taskManager.removeChecked()

class reset(CommandInterface):
    def __init__(self, taskManager):
        self.taskManager = taskManager

    def apply(self):
        ioManager = IOManager()
        if ioManager.readConfirmation("Are you sure?"):
            return self.taskManager.reset()
        else:
            return 0