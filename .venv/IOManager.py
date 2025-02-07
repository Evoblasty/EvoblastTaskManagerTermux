class IOManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def readInput(self,msg):
        result = input(msg)
        if result:
            return result
        else:
            print("Error: Empty line")
            return None

    def readConfirmation(self,msg):
        userInput = ""
        result = False
        finishCondition = False
        while not finishCondition:
            userInput = input(msg+" y/n:")
            if userInput == "y":
                result = True
                finishCondition = True
            elif userInput == "n":
                finishCondition = True
            else:
                print("Error: Please enter the character y or n")
        return result