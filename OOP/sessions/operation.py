from employer import Emp


class Operation:
    lEmp = []

    def ajouterEmp(self):
        c = input("cin ")
        n = input("nom ")
        p = input("prenom ")
        s = float(input("salaire "))
        a = int(input("year "))
        m = int(input("month "))
        j = int(input("day "))
        e = Emp(c, n, p, s, a, m, j)
        self.lEmp.append(e)
        print("AJOUTE AVEC SUCCEE")

    def afficher(self):
        for i in range(len(self.lEmp)):
            print(self.lEmp[i].__str__())

    def trieParDate(self):
        temp = 0
        for i in range(len(self.lEmp)):
            for j in range(len(self.lEmp)-1):
                if self.lEmp[j].date_amb > self.lEmp[j+1].date_amb:
                    temp = self.lEmp[j].date_amb
                    self.lEmp[j].date_amb = self.lEmp[j+1].date_amb
                    self.lEmp[j+1].date_amb = temp

    def surprimer(self):
        pos = int(input("0 1 2 ? "))
        for i in range(pos, len(self.lEmp)-1):
            self.lEmp[i] = self.lEmp[i+1]
        taille = len(self.lEmp)-1
        self.lEmp = self.lEmp[:taille]

    def modifier(self):
        pos = int(input("0 1 2 ? "))
        for i in range(len(self.lEmp)):
            if i == pos:
                newS = float(input("entrer le salaire: "))
                self.lEmp[i].SALAIRE = newS
                break
