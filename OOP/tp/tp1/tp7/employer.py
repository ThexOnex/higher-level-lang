from abc import ABC, abstractmethod


class Employer:
    matricule: str
    nom: str
    prenom: str
    heure_arrivee: str

    def __init__(self, m, n, p, h) -> None:
        self.matricule = m
        self.nom = n
        self.prenom = p
        self.heure_arrivee = h

    @abstractmethod
    def afficher_details(self):
        pass
        # print("matricule ", self.matricule, "nom: ", self.nom, " prenom: ",
        #       self.prenom, " heure d'arrive: ", self.heure_arrivee)
