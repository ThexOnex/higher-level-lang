from abc import ABC, abstractmethod


class Person(ABC):
    nom: str
    prenom: str
    genre: str

    def __init__(self, n, p, g):
        super().__init__()
        self.nom = n
        self.prenom = p
        self.genre = g

    def __str__(self) -> str:
        return f"le nom: {self.nom} le prenom: {self.prenom} le genre: {self.genre}"

    @abstractmethod
    def calculerSalaire(self):
        pass

    @abstractmethod
    def calculerEnciente(self):
        pass
