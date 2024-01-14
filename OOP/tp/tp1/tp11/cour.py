class Cours:
    def __init__(self, n, e, et) -> None:
        self.nom = n
        self.enseignant = e
        self.etudiants_inscrits = et

    def __str__(self) -> str:
        return self.nom, ",", self.enseignant.nom, ",", self.etudiants_inscrits

    def ajouterInscrire(self, i):
        i.etudiants_inscrits = True

    def désinscrire(self, i):
        i.etudiants_inscrits = False

    def afficherDetails(self):
        print(self.nom, ",", self.enseignant.nom, ",", end='')
        if self.etudiants_inscrits == True:
            print("l'etudient est s'inscrits")
        else:
            print("l'etudient est n'est pas s'inscrits")
