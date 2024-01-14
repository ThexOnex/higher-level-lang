class Contreleur:
    def __init__(self, p: list, c) -> None:
        self.personnes = p
        self.conges = c

    def afficherEmployers(self):
        for i in self.personnes:
            print(i.__str__())

    def ajouterPersonne(self, person):
        self.personnes.append(person)

    def surprimerPerson(self, person):
        self.personnes.remove(person)

    def modifierPerson(self, index):
        stop = False
        while (not stop):
            choice = input(
                "do you want to change work hours/prime money(entre 'hs' or 'prime') or the base salary(entre 'salary') ")
            if choice == "salary":
                self.personnes[index].salaire_de_base = float(
                    input("Entre the base salary of the employer "))
                break
            elif choice == "hs":
                self.personnes[index].hs = float(
                    input("Entre work hours of the employer "))
                break

            elif choice == "prime":
                self.personnes[index].prime = float(
                    input("Entre the prime money of the employer "))
                break
            else:
                continue

    def chercherParCin(self, string):
        for i in self.personnes:
            if i.cin == string:
                print("we found the employer", i.__str__())
        else:
            print("We haven't found any employer")

    def trieeParDate(self):
        for i in range(len(self.personnes)):
            for j in range(len(self.personnes)-1):
                if self.personnes[j].date_of_hire > self.personnes[j+1].date_of_hire:
                    temp = self.personnes[j]
                    self.personnes[j] = self.personnes[j+1]
                    self.personnes[j+1] = temp

    def ajouterConge(self, congee):
        self.conges.append(congee)
        print("conge added successfully")
        if self.conges[len(self.conges)-1].calculerNombreDeJour() > 25:
            print("---- Number of days more than 25 days is not allowed ----")
            self.conges.pop(len(self.conges)-1)

    def modifierConge(self, index):
        stop = False
        while (not stop):
            choice = input(
                "do you want to change the start date and the end date of the holiday (entre 'start' or 'end') or the Id (entre 'id') ")
            # if choice == "start":
            #     self.personnes[index].dateDebut = input("Entre the base salary of the employer ")
            #     break
            # elif choice == "end":
            #     self.personnes[index].dateFin = input("Entre work hours of the employer ")
            #     break

            if choice == "id":
                self.personnes[index].idConge = input(
                    "Entre the prime money of the employer ")
                break
            else:
                print("try again")
                continue

    def afficherConge(self):
        for i in self.conges:
            print(i.__str__())

    def sauvegarderDansUnFishier(self):
        f = open("c://congee.txt", "w")
        for i in self.conges:
            f.write(i.__str__())
            f.write("\n")
        f.close()
        print("list added to congee.txt successfully")
