from vehi import Vehicule
from es import Essence


class VoitureCarburant(Vehicule, Essence):
    def __init__(self, m, r, d, p) -> None:
        super().__init__(m, r, d)
        self.prix = p

    def type_diesle(self):
        return "type carburant essance"

    def consommation(self):
        return "50 litre par 100 km"

    def caracteri(self):
        return self.type_diesle(), self.consommation()

    def __str__(self) -> str:
        return super().__str__(), self.prix, self.caracteri()
