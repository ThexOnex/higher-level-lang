class Contreleur:
    majeur = []

    def __init__(self, p) -> None:
        self.people = p

    def afficherDetails(self):
        for i in self.people:
            print(i.__str__())

    def trier_la_liste_par_nom(self):
        for i in range(len(self.people)):
            for j in range(len(self.people)):
                if self.people[j].nom > self.people[j+1].nom:
                    temp = self.people[j]
                    self.people[j] = self.people[j+1]
                    self.people[j+1] = temp

    def filtrerlesEtudiant(self):
        for i in self.people:
            if i.calculer_moyenne() > 15:
                Contreleur.majeur.append(i)
        for i in Contreleur.majeur:
            print(i.__str__())

    def ajouter(self, per):
        self.people.append(per)

    def retirer(self, per):
        self.people.remove(per)
