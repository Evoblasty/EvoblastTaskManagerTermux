from itertools import filterfalse
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
        else:
            print("Error adding task")

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
        else:
            print("Error deleting task")

    def printList(self):
        numerator = 1
        print("")
        for t in self.list:
            print(str(numerator)+". "+t.toBasicString())
            numerator = numerator + 1
        print("")

    def checkTask(self,name):
        if self.isInList(name):
            task = self.get(name)
            task.check()
            print("Task checked")
        else:
            print("Error checking task")

    def removeChecked(self):
        for t in reversed(self.list):
            if t.status is True:
                self.list.remove(t)
                print("Task "+t.name+" removed correctly")


    def reset(self):
        self.list = []
        print("List cleared")




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