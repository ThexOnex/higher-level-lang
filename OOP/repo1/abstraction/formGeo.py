from abc import ABC, abstractmethod


class FormGeometrique(ABC):
    @abstractmethod
    def afficher(self):
        pass

    @abstractmethod
    def calculerSurface(self):
        pass
