from villa import Villa
from appartement import Appartement


class Contreleur:
    villa = []
    appartement = []

    def __str__(self):
        return f"{self.villa}\n {self.appartement}"

    def ajouter_appar(self, Appartement):
        self.villa.append(Appartement)

    def ajouter_villa(self, Villa):
        self.appartement.append(Villa)
