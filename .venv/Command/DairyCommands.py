from Command.CommandInterface import CommandInterface
from IOManager import IOManager

class fillMorning(CommandInterface):
    def __init__(self,morning):
        self.morning = morning

    def apply(self):
        ioManager = IOManager()
        self.morning.w = True
        purpose = ioManager.readInput("What is today's purpose:")
        if purpose:
            self.morning.setPurpose(purpose)
        virtue = ioManager.readOption("What virtue will be practiced",["wisdom","justice","courage","temperance"])
        self.morning.setVirtue(virtue)

class fillEvening(CommandInterface):
    def __init__(self,evening):
        self.evening = evening

    def apply(self):
        ioManager = IOManager()
        self.evening.w = True
        self.evening.setAction(ioManager.readOption("What are today's actions based on?",["reason","emotion"]))
        self.evening.setReaction(ioManager.readConfirmation("Are events beyond your control causing a reaction?"))
        self.evening.setVersion(ioManager.readConfirmation("Are you the best version of yourself right now?"))

class fillNight(CommandInterface):
    def __init__(self,night,morning):
        self.night = night
        self.morning = morning

    def apply(self):
        ioManager = IOManager()
        self.night.w = True
        goods = ioManager.readInput("What things were done right today?:")
        if goods:
            self.night.setGoods(goods)
        better = ioManager.readInput("What things could have been done better today?:")
        if better:
            self.night.setBetter(better)
        learning = ioManager.readInput("What was learned today?:")
        if learning:
            self.night.setLearning(learning)
        if self.morning.getVirtue():
            self.night.setVirtue(ioManager.readConfirmation("Did you develop "+self.morning.getVirtue()+" today?:"))
        self.night.setDeath(ioManager.readConfirmation("If today was your last day, would you be proud?:"))

class showToday(CommandInterface):
    def __init__(self,day):
        self.day = day
    def apply(self):
        done = " "
        if self.day.morning.w:
            done = "X"
        print("["+done+"] Morning")
        done = " "
        if self.day.evening.w:
            done = "X"
        print("[" + done + "] Evening")
        done = " "
        if self.day.night.w:
            done = "X"
        print("[" + done + "] Night")

class saveToday(CommandInterface):
    def __init__(self,day,filemanager):
        self.filemanager = filemanager
        self.day = day

    def apply(self):
        self.filemanager.saveDaily(self.day)