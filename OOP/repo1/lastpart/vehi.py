from abc import ABC, abstractmethod


class Vehicule(ABC):
    def __init__(self, m, r, d) -> None:
        self.matricule = m
        self.mark = r
        self.modele = d

    def __str__(self) -> str:
        return f"maricule: {self.matricule} mark: {self.mark} modele: {self.modele}"

    @abstractmethod
    def caracteri(self):
        pass
