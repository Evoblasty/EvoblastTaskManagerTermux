from Command.CommandInterface import CommandInterface
from IOManager import IOManager

class openToDoList(CommandInterface):
    def __init__(self,tasker):
        self.tasker = tasker

    def apply(self):
        self.tasker.executionLoop()