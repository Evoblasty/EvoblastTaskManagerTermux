from IOManager import IOManager
class Menu:
    def __init__(self,commandList,name,GreetMsg=None):
        self.commands = {com.toString(): com for com in commandList}
        self.IOmanager = IOManager()
        self.name = name
        if GreetMsg is not None:
            self.GreetMsg = GreetMsg
        else:
            self.GreetMsg = name

    def executionLoop(self):
        exitVal = False
        print(self.GreetMsg)
        while not exitVal:
            wanted = self.IOmanager.readInput("Command:")
            if self.checkForInt(wanted):
                if int(wanted) > 0 and int(wanted) <= len(self.commands):
                    self.commands[list(self.commands.keys())[int(wanted)-1]].apply()
                elif int(wanted)==len(self.commands)+1:
                    exitVal = True
                else:
                    print("Error: Command out of bounds")
            else:
                if wanted in self.commands:
                    self.commands[wanted].apply()
                elif wanted == "exit":
                    exitVal = True
                elif wanted == "help":
                    self.showList()
                else:
                    print("Error: Unknown command. Try help to check command list")
        print("Closed "+self.name)


    def showList(self):
        cmdList = list(self.commands.keys())
        i = 1
        for c in cmdList:
            print(str(i)+". "+c)
            i = i+1
        print(str(i)+". exit")


    def checkForInt(self,w):
        try:
            num = int(w)
            return True
        except ValueError:
            return False


class MenuSave(Menu):

    def __init__(self,commandList,name,saveCommand,LoadComand):
        super().__init__(commandList,name)
        self.commands["save"] = saveCommand
        self.loader = LoadComand
        self.changes = 0

    def executionLoop(self):
        self.loader.apply()
        exitVal = False
        while not exitVal:
            wanted = self.IOmanager.readInput("Command:")
            if self.checkForInt(wanted):
                if int(wanted) > 0 and int(wanted) <= len(self.commands):
                    self.changes = self.changes + self.commands[list(self.commands.keys())[int(wanted) - 1]].apply()
                    if int(wanted)==len(self.commands):
                        self.changes = 0
                elif int(wanted) == len(self.commands)+1:
                    if self.changes > 0:
                        self.unsavedChanges()
                    exitVal = True
                else:
                    print("Error: Command out of bounds")
            else:
                if wanted in self.commands:
                    self.changes = self.changes + self.commands[wanted].apply()
                    if wanted == "save":
                        self.changes = 0
                elif wanted == "exit":
                    if self.changes > 0:
                        self.unsavedChanges()
                    exitVal = True
                elif wanted == "help":
                    self.showList()
                else:
                    print("Error: Unknown command. Try help to check command list")
        print("Closed "+self.name)


    def unsavedChanges(self):
        msg = "There are "+str(self.changes)+" unsaved changes, would you like to save them?"
        if self.IOmanager.readConfirmation(msg):
            self.commands["save"].apply()
        else:
            print("Changes not saved")