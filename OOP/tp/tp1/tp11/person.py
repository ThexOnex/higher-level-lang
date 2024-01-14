from abc import ABC, abstractmethod


class Personne:
    def __init__(self, nom, prenom, age) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def __str__(self) -> str:
        return self.nom, self.prenom , self.age

    @abstractmethod
    def gererUrgence(self):
        pass

    @abstractmethod
    def gererAdress(self):
        pass
