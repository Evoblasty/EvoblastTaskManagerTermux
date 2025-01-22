class Task:
    def __init__(self,name,status=False):
        self.name = name
        if status is False:
            self.status = False
        elif status == "False":
            self.status = False
        elif status == "True":
            self.status = True


    def print(self):
        print(self.name + ", " + str(self.status))

    def toStringCSV(self):
        return f"{self.name};{self.status}"

    def check(self):
        self.status = True

    def toBasicString(self):
        box = "[ ]"
        if self.status is True:
            box = "[X]"
        return self.name + " " + box