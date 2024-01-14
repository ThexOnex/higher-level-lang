from person import Personne


class Etudiant(Personne):
    def __init__(self, nom, prenom, age, n) -> None:
        super().__init__(nom, prenom, age)
        self.notes = n

    def __str__(self) -> str:
        return super().__str__(), self.notes

    def calculer_moyenne(self):
        sum = 0
        for i in self.notes:
            sum += i
        return sum/len(self.notes)

    def gererUrgence(self):
        return "07364832"

    def gererAdress(self):
        return "8000 5B"
