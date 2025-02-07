from abc import ABC, abstractmethod

class CommandInterface(ABC):
    @abstractmethod
    def apply(self):
        pass

    def toString(self):
        return self.__class__.__name__
