class GestionAeroport:
    vols: list

    def __init__(self, v) -> None:
        self.vols = v

    def afficherDesVols(self):
        print("les details des vols: ")
        for i in self.vols:
            i.afficher_details()

    def ajouterUnVol(self, vol):
        self.vols.append(vol)
        print("vol a ete cree")

    def retirerUnVol(self, vol):
        self.vols.remove(vol)
        print("vol a ete surprimer ")

    def trieParheure(self):
        for i in range(len(self.vols)):
            for j in range(len(self.vols)-1):
                if self.vols[j].heure_depart > self.vols[j+1].heure_depart:
                    temp = self.vols[j]
                    self.vols[j] = self.vols[j+1]
                    self.vols[j+1] = temp
        print("les details des vols tries : ")
        for i in self.vols:
            print(i.__str__())
