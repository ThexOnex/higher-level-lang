class Livre:
    def __init__(self, t: str, a: str, an: int):
        self.titre = t
        self.auteur = a
        self.annee = an
        self.genre = []

    def afficher_info(self):
        print("titre: ", self.titre, "auteur: ",
              self.auteur, "annee: ", self.annee)
