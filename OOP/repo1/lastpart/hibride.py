from es import Essence
from vehi import Vehicule
from int import Electrique

#abstract interface interface
class Hybrid(Vehicule, Essence, Electrique):
    def __init__(self, m, r, d, p, du) -> None:
        super().__init__(m, r, d)
        self.prix = p
        self.durre_Vie = du

    def type_diesle(self):
        return "Utilisee type carburant(Essance)"

    def consommation(self):
        return "60 l pour 60km"

    def type_electrique(self):
        return "mode electrique"

    def durreDeVie(self):
        return self.durre_Vie

    def caracteri(self):
        return self.type_diesle(), self.consommation(), self.type_electrique(), self.durreDeVie()

    def __str__(self) -> str:
        return super().__str__(), f"prix: {self.prix} duree de vie: {self.durre_Vie}, cara: {self.caracteri()}"
