class GestionPointage:
    def __init__(self, p) -> None:
        self.pointages = p

    def ajouterUnpointage(self, poin):
        self.pointages.append(poin)

    def retirerDesEmployer(self, poin):
        self.pointages.remove(poin)

    def afficher_list_demployer(self):
        print("la list des employers: ")
        for i in self.pointages:
            print(i.employe.nom, "et prenom: ", i.employe.prenom)

    def chargerUneList(self):
        TheList = []
        f = open("c://employers.txt", "r")
        lines = f.readlines()
        for line in lines:
            string = line.strip().split(",")
            TheList.append(string)
        return TheList

    def nombreTotalTravailParJour(self):
        hours = 0
        minutes = 0
        for i in self.pointages:
            nombre = i.calculerLesHeursTravail().split(":")
            hour = int(nombre[0])
            minute = int(nombre[1])
            hours += hour
            minutes += minute
        if minutes >= 60:
            # 120
            howmanys = minutes/60
            minutes -= (int(howmanys) * 60)
            hours += int(howmanys)
        return str(hours)+":"+str(minutes)

    def moyenHeurTravailleParJour(self):
        string = self.nombreTotalTravailParJour().split(":")

        return int(string[0])/len(self.pointages)

    def employerAvecPlusGrandeHrurs(self):
        nombre = self.pointages[0].calculerLesHeursTravail().split(":")
        plushour = int(nombre[0])
        plusminute = int(nombre[1])
        winner = self.pointages[0].employe.nom
        for i in self.pointages:
            nombre = i.calculerLesHeursTravail().split(":")
            hour = int(nombre[0])
            if hour > plushour:
                plushour = hour
                winner = i.employe.nom
            elif hour == plushour:
                minute = int(nombre[1])
                if minute > plusminute:
                    plusminute = minute
                    winner = i.employe.nom
        return winner
