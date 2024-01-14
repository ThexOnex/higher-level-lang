from abc import ABC, abstractmethod


class Electrique(ABC):
    @abstractmethod
    def type_electrique(self):
        pass

    @abstractmethod
    def durreDeVie(self):
        pass
