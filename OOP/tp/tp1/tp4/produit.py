class Produit:
    nom: str
    prix: float
    quantite_en_stock: float
    promotion: bool

    def __init__(self, n, p, q):
        self.nom = n
        self.prix = p
        self.quantite_en_stock = q
        self.promotion = False

    def ajusterQuantite(self, quantite):
        self.quantite_en_stock = quantite

    def afficher(self):
        print("nom est ", self.nom, "le prix est",
              self.prix, "la quantite en stock est : ", self.quantite_en_stock)

    def enregistreFishier(self, letter):
        f = open("c://produit.txt", letter)
        f.write("produit normal \n")
        f.write(self.nom)
        f.write("\n")

        f.write(str(self.prix))
        f.write("\n")

        f.write(str(self.quantite_en_stock))
        f.write("\n")
        f.close

    def chargerInfo(self):
        f = open("c://product.txt", "r")
        L = f.read()
        t = str(L).split("\n")
        self.nom = t[0]
        self.prix = t[1]
        self.quantite_en_stock = t[2]
    # def rechercherParNom(self,list):

    def modifierInfo(self, name, price, quantite):
        self.nom = name
        self.prix = price
        self.quantite_en_stock = quantite

    def promotionP(self, per):
        self.prix -= self.prix * per/100
        self.promotion = True
