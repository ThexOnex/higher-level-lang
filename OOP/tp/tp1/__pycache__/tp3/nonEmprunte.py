from livre import Livre
class LivreEmpruntable(Livre):
    disponible: bool

    def __init__(self, e: bool):
        super().__init__()
        self.disponible = e

    def emprunter(self):
        self.disponible = True
        print("le livre a ete empruntee")

    def retourner(self):
        self.disponible = False
        print("le livre a ete retourner")
