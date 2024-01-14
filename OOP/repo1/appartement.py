from li3jbk import Immobilier


class Appartement(Immobilier):
    prix: float
    nbj: int

    def __init__(self, t, a, s, p, nbj=0):
        super().__init__(t, a, s)
        self.prix = p
        self.nbj = nbj

    def __str__(self):
        if self.nbj == 0:
            return f"appartement : {super().__str__()} est disponible"
        return f"appartement : {super().__str__()} {self.nbj} jours avec un prix:  {self.prix}  TOTAL: {self.totalPrix()}"

    def totalPrix(self):
        return self.nbj * self.prix
