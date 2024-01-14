from produit import Produit
import datetime


class ProduitAlimentaire(Produit):
    date_de_expiration: datetime
    promotion: bool

    def __init__(self, n, p, q, a, m, d):
        super().__init__(n, p, q)
        self.date_de_expiration = datetime.date(a, m, d)
        self.promotion = False

    def ajusterQuantite(self, quantite):
        self.quantite_en_stock = quantite

    def afficher(self):
        print(super().afficher(), " la date de expiration: ",
              self.date_de_expiration)

    def enregistreFishierAli(self, letter):
        f = open("c://produit.txt", letter)
        f.write("produit alimentaire: \n")
        f.write(self.nom)
        f.write("\n")
        f.write(str(self.prix))
        f.write("\n")
        f.write(str(self.quantite_en_stock))
        f.write("\n")

        f.write(str(self.date_de_expiration))
        f.write("\n")
        f.close

    def chargerInfoAli(self):
        f = open("c://produitAli.txt", "r")
        L = f.read()
        t = str(L).split("\n")
        self.nom = t[0]
        self.prix = t[1]
        self.quantite_en_stock = t[2]
        self.date_de_expiration = t[3]

    def modifierInfo(self, name, price, quantite, a, m, j):
        super().modifierInfo(name, price, quantite)
        self.date_de_expiration = datetime.date(a, m, j)

    def promotionP(self, per):
        self.prix -= self.prix * per/100
        self.promotion = True

    def verificationDExpiration(self, current_date):
        if self.date_de_expiration > current_date:
            print("Product is NOT expired")
        else:
            print("Product is expired")
