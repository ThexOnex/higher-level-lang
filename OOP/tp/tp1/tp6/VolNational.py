from vol import Vol


class VolNational(Vol):
    ville_arrivee: str

    def __init__(self, n, c, h, hd, p, ville) -> None:
        super().__init__(n, c, h, hd, p)
        self.ville_arrivee = ville

    def __str__(self):
        return f"numero: {self.numero_vol}  compagnie:  {self.compagnie_aerienne}  heure de depart : {self.heure_depart} heure d arrive: {self.heure_arrivee} porte d'embarquement: {self.porte_embarquement} pays d'arrive: {self.ville_arrivee}"
