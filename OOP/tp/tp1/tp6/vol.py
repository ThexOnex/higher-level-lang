from abc import ABC, abstractmethod


class Vol:
    numero_vol: int
    compagnie_aerienne: str
    heure_depart: int
    heure_arrivee: int
    porte_embarquement: str

    def __init__(self, n, c, h, hd, p) -> None:
        self.numero_vol = n
        self.compagnie_aerienne = c
        self.heure_arrivee = h
        self.heure_depart = hd
        self.porte_embarquement = p

    @abstractmethod
    def __str__(self):
        pass
        # print(f"le numero du vol: {self.numero_vol} et la compagnie arrienne: {self.compagnie_aerienne} l heure de depart:
        #       {self.heure_depart} et l heur d arrivee {self.heure_arrivee} avec la porte d embarquement est {self.porte_embarquement}")
