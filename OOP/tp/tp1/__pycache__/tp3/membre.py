class Membre:
    def __init__(self, n: str, a: str, nbr):
        self.nom = n
        self.auteur = a
        self.nombre = nbr

    def afficherMembre(self):
        print("nom: ", self.nom, "auteur: ", self.auteur,
              "le nombre maximal de livres empruntables", self.nombre)
        if self.nombre > 6:
            print("il a atteint le nombre maximal de livres empruntés 6")
            self.nombre = 6
