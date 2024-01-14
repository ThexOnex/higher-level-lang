class GestionAeroportFichier:
    def __init__(self, v: list, vl: list) -> None:
        self.vols = v
        self.listedVols = vl

    def sauvgarder(self):
        f = open("c://vols.txt", "a")
        for i in self.vols:
            f.write(i.__str__())
            f.write("\n")
        f.close()
        print("fishier a ete sauvegarder")

    def charger(self):
        f = open("c://vols.txt", "r")
        file = f.read()
        lines = file.split("\n")
        self.listedVols = [0]*len(lines)

        for i in range(len(lines)-1):
            self.listedVols[i] = lines[i]
        print("fishier a ete charger")

    def afficherLesCHarger(self):
        for i in self.listedVols:
            print(i.__str__())
