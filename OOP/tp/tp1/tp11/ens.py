from person import Personne


class Enseignant(Personne):
    def __init__(self, nom, prenom, age, m) -> None:
        super().__init__(nom, prenom, age)
        self.matieres_enseignees = m

    def __str__(self) -> str:
        return super().__str__(), self.matieres_enseignees

    def gererUrgence(self):
        return "06645542"

    def gererAdress(self):
        return "5000 3A"
