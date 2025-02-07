from fcntl import FASYNC
from itertools import filterfalse, chain
from operator import contains
from Task import Task
from FileManager import FileManager

class TaskManager:
    def __init__(self,list=None):
        if list is not None:
            self.list=list
        else:
            self.list = []

    def addTask(self,name,status=False):
        if not self.isInList(name):
            task = Task(name,status)
            self.list.append(task)
            print("Task added succesfully")
            return 1
        else:
            print("Error adding task")
            return 0

    def isInList(self,key):
        result = False
        for t in self.list:
            if t.name == key:
                result = True

        return result

    def get(self,key):
        for t in self.list:
            if t.name == key:
                return t

    def removeTask(self,name):
        if self.isInList(name):
            task = self.get(name)
            self.list.remove(task)
            print("Task removed successfully")
            return 1
        else:
            print("Error deleting task")
            return 0

    def printList(self):
        if len(self.list) == 0:
            print("")
            print("The list is empty")
            print("")
        else:
            numerator = 1
            undone = 0
            print("")
            for t in self.list:
                print(str(numerator)+". "+t.toBasicString())
                numerator = numerator + 1
                if t.status is False:
                    undone = undone +1
            print("")
            print(str(undone)+" task remaining")
            print("")

    def checkTask(self,name):
        if self.isInList(name):
            task = self.get(name)
            task.check()
            print("Task checked")
            return 1
        else:
            print("Error checking task")
            return 0

    def removeChecked(self):
        changes = 0
        for t in reversed(self.list):
            if t.status is True:
                self.list.remove(t)
                print("Task "+t.name+" removed correctly")
                changes = changes+1
        return changes


    def reset(self):
        changes = len(self.list)
        self.list = []
        print("List cleared")
        return changes




"""
taskmanager = TaskManager()
taskmanager.addTask("Prueba 1")
taskmanager.addTask("Prueba 2")
taskmanager.printList()
taskmanager.removeTask("Prueba 3")
taskmanager.removeTask("Prueba 1")
taskmanager.printList()
taskmanager.addTask("Prueba 4", status=True)
fileManager = FileManager()
fileManager.saveList(taskmanager.list)
print("taskmanager2")
taskmanager2 = TaskManager(fileManager.loadList())
taskmanager2.printList()
"""