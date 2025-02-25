from datetime import date
from setuptools.glob import glob0


class Morning:
    def __init__(self,w=False,purpose="",virtue=""):
        self.w = w
        self.purpose = purpose
        self.virtue = virtue

    def setPurpose(self,purpose):
        self.purpose = purpose

    def setVirtue(self,virtue):
        match virtue:
            case 1:
                self.virtue = "Wisdom"
            case 2:
                self.virtue = "Justice"
            case 3:
                self.virtue = "Courage"
            case 4:
                self.virtue = "Temperance"
            case _:
                self.virtue = ""

    def getVirtue(self):
        return self.virtue


class Evening:
    def __init__(self,w=False,action="",reaction="",version=""):
        self.w = w
        self.action = action
        self.reaction = reaction
        self.version = version

    def setAction(self,action):
        match action:
            case 1:
                self.action = "Reason"
            case 2:
                self.action = "Emotion"
            case _:
                self.action = ""

    def setReaction(self,reaction):
        match reaction:
            case True:
                self.reaction = "Yes"
            case False:
                self.reaction = "No"
            case _:
                self.reaction = ""

    def setVersion(self,version):
        match version:
            case True:
                self.version = "Yes"
            case False:
                self.version = "No"
            case _:
                self.version = ""


class Night:
    def __init__(self,w=False,goods="",better="",learning="",virtue="",death=""):
        self.w = w
        self.goods = goods
        self.better = better
        self.learning = learning
        self.virtue = virtue
        self.death = death

    def setGoods(self,goods):
        self.goods = goods

    def setBetter(self,better):
        self.better = better

    def setLearning(self,learning):
        self.learning = learning

    def setVirtue(self,virtue):
        match virtue:
            case True:
                self.virtue = "Yes"
            case False:
                self.virtue = "No"
            case _:
                self.virtue = ""

    def setDeath(self,death):
        match death:
            case True:
                self.death = "Yes"
            case False:
                self.death = "No"
            case _:
                self.death = ""

class Day:
    def __init__(self,dateDiary=None,morning=None,evening=None,night=None):
        if dateDiary is None:
            self.date = date.today()
        else:
            self.date = dateDiary
        if morning is None:
            self.morning = Morning()
        else:
            self.morning = morning
        if evening is None:
            self.evening = Evening()
        else:
            self.evening = evening
        if night is None:
            self.night = Night()
        else:
            self.night = night