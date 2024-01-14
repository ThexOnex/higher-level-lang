from villa import Villa
from appartement import Appartement
from li3jbk import Immobilier
import pickle


class Methode:
    immo = []

    def creeImmo(self):
        app = Appartement("titre appartement", "adress app", 576, 555)
        vill = Villa("titre villa", "adress villa", 333, 666, 5)
        app2 = Appartement("titre appartement 2", "adress app 2", 696, 855, 20)
        vill2 = Villa("titre villa 2", "adress villa 2", 333, 166, 7, 40)
        self.immo.append(app)
        self.immo.append(vill)
        self.immo.append(app2)
        self.immo.append(vill2)
        print("Immobilier cree")

    def affichierTous(self):
        for i in range(len(self.immo)):
            print(self.immo[i].__str__())

    def verifier(self, obj):
        if isinstance(obj, Immobilier):
            return True
        return False

    def affichierApp(self):
        for i in range(len(self.immo)):
            if isinstance(self.immo[i], Appartement):
                print(self.immo[i].__str__())

    def affichierVill(self):
        for i in self.immo:
            if isinstance(i, Villa):
                print(i.__str__())

    def sauvgarderFishierObjet(self):
        f = open("c://pickle2.pkl", "ab")
        for i in range(len(self.immo)):
            # serilisation ==> converti binaire
            pickle.dump(self.immo[i], f)
            print("sauvegarder avec succees")
        print("fishier cree avec succee")

    def lireFishierObjet(self):
        f = open("c://pickle2.pkl", "rb")
        while f != None:
            try:
                r = pickle.load(f)
                print(r)
            except EOFError:
                pass
