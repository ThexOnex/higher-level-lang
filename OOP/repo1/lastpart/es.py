from abc import ABC, abstractmethod


class Essence(ABC):
    @abstractmethod
    def type_diesle(self):
        pass

    @abstractmethod
    def consommation(self):
        pass
