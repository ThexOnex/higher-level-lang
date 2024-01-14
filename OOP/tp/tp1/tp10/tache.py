class Tache:
    def __init__(self, d, e) -> None:
        self.description = d
        self.etat = e

    def afficher(self):
        print(f"the task is:   {
              self.description} the state of the task: {self.etat}")
