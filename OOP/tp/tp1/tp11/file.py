class GestionEducationFichier:
    def __init__(self, edu, c) -> None:
        self.people = edu
        self.cours = c

    def sauvegarder(self):
        f = open("educateur.txt", "w")
        for i in self.people:
            f.write(i.__str__())
        f.write("=============")
        for i in self.cours:
            f.write(i.__str__())
