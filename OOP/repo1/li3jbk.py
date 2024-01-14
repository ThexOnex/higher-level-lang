class Immobilier:
    titre: str
    adress: str
    superficie: float

    def __init__(self, t, a, s):  # contrecteur explicite(self,dm,s,w)
        self.titre = t
        self.adress = a
        self.superficie = s

    def __str__(self):
        return f"{self.titre} {self.adress} {self.superficie}"

    # def getTitre(self):
    #     return self.__titre

    # def setTitre(self, T):
    #     self.__titre = T

    # def getAdress(self):
    #     return self._adress

    # def setAdress(self, A):
    #     self._adress = A

    # def getSup(self):
    #     return self._superficie

    # def setSup(self, S):
    #     self._superficie = S

    # def totalPrix(self):  # non definie
    #     pass
