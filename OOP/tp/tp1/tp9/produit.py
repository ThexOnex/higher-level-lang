class Produit:
    def __init__(self, n, p, q):
        self.nom = n
        self.prix = p
        self.quantite_en_stock = q

    def afficher(self):
        print("nom: ", self.nom, "prix: ", self.prix,
              "quantite en stock: ", self.quantite_en_stock)
