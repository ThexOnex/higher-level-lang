from produit import Produit


class ProduitElectronique(Produit):
    garantie: int
    promotion: bool

    def __init__(self, n, p, q, g):
        super().__init__(n, p, q)
        self.garantie = g
        self.promotion = False

    def afficher(self):
        print(f"{super().afficher()} et la garantie est {self.garantie}")

    def ajusterQuantite(self, quantite):
        self.quantite_en_stock = quantite

    def enregistreFishierEle(self, letter):
        f = open("c://produit.txt", letter)
        f.write("produit electronique: \n")
        f.write(self.nom)
        f.write("\n")

        f.write(str(self.prix))
        f.write("\n")

        f.write(str(self.quantite_en_stock))
        f.write("\n")

        f.write(str(self.garantie))
        f.write("\n")
        f.close

    def chargerInfoEle(self):
        f = open("c://produitEle.txt", "r")
        L = f.read()
        t = str(L).split("\n")
        self.nom = t[0]
        self.prix = t[1]
        self.quantite_en_stock = t[2]
        self.garantie = t[3]

    def modifierInfo(self, name, price, quantite, garantie):
        super().modifierInfo(name, price, quantite)
        self.garantie = garantie

    def promotionP(self, per):
        self.prix -= self.prix * per/100
        self.promotion = True
