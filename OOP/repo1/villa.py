from li3jbk import Immobilier


class Villa(Immobilier):
    prix: float
    nbj: int
    cotion: float

    def __init__(self, t, a, s, p, c, nbj=0):
        super().__init__(t, a, s)
        self.prix = p
        self.nbj = nbj
        self.cotion = c

    def __str__(self):
        if self.nbj == 0:
            return f"villa :  {super().__str__()}est disponible"
        return f"villa : {super().__str__()}est reservee pendant {self.nbj} jours avec un prix: {self.prix}  TOTAL: {self.totalPrix()}"

    def totalPrix(self):
        return (self.nbj * self.prix) + self.cotion
