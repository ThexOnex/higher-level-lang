from stock import StockInsuffisant


class Panier:
    def __init__(self, p: list):
        self.Produits = p

    def ajouterProduct(self, produit):
        self.Produits.append(produit)

    def calculerTotalProduits(self):
        return len(self.Produits)+1

    def passerCommande(self):
        commande = input("Entrer le produit ")
        for i in self.Produits:
            if i.quantite_en_stock > 0:
                if i.nom == commande:
                    print("le prix de votre commande est: ", i.prix)
                    try:
                        nombre_pr = int(
                            input("Entrer le nombre des produits: "))
                        if nombre_pr > 0 or i.quantite_en_stock > nombre_pr:
                            raise StockInsuffisant()
                        else:
                            i.quantite_en_stock -= nombre_pr
                            print("purchase")
                    except Exception as quantite:
                        print(quantite)
            else:
                print("on a pas trouve ce produit")

    def afficherProducts(self):
        print("===================list of products================")
        for i in self.Produits:
            print(i.afficher())
