from produit import Produit
from produitAli import ProduitAlimentaire
from produitEle import ProduitElectronique


class Method:
    produits = []
    archive = []

    def __init__(self, list, list2):
        self.produits = list
        self.archive = list2

    def rechercherParNom(self, name):
        for i in self.produits:
            if name in i.nom:
                print("On a trouvee le produit ")
                i.afficher()
                break
        else:
            print("on n'a pas trouvee le produit")

    def surprimeProduit(self, name):
        for i in self.produits:
            if name == i.nom:
                self.produits.remove(i)
                print("le produit a ete surprimer")
                break
        else:
            print("On n a pas trouver le produit")

    def trieProducts(self):
        for i in range(len(self.produits)):
            for j in range(len(self.produits)-1):
                if self.produits[j].prix > self.produits[j+1].prix:
                    temp = self.produits[j]
                    self.produits[j] = self.produits[j+1]
                    self.produits[j+1] = temp

    def afficherList(self):
        for i in self.produits:
            i.afficher()

    def filtrer(self, CLASS):
        for i in self.produits:
            if isinstance(i, CLASS):
                i.afficher()

    def afficherProduitEnPromotion(self):
        print("les produits en promotion sont: ")
        for i in range(len(self.produits)):
            if self.produits[i].promotion:
                self.produits[i].afficher()

    def archiverUnProduit(self, index):
        self.archive.append(self.produits[index-1])
        self.produits.pop(index-1)

    def restaurerUnProduit(self, index):
        self.archive.pop(index-1)
        self.produits.append(index-1)

    def afficherProduitArchiver(self):
        print("des produits archives sont: ")
        for i in self.archive:
            i.afficher()

    def LePrixMoyen(self):
        max_price = 0.0
        for i in range(len(self.produits)):
            max_price += self.produits[i].prix
        return max_price/len(self.produits)

    def QuantiteTotalEnStock(self):
        max_Q = 0.0
        for i in range(len(self.produits)):
            max_Q += self.produits[i].quantite_en_stock
        return max_Q

    def detectDouble(self):
        print("detectation des produits doubles...")
        for i in range(len(self.produits)):
            for j in range(i+1, len(self.produits)):
                if self.produits[i].nom == self.produits[j].nom:
                    print("double detected!!!!!!")
                    print(self.produits[i].nom)
            # if self.produits[i].quantite_en_stock > self.produits[j].quantite_en_stock:
            #     self.produits[i].quantite_en_stock += self.produits[j].quantite_en_stock
            #     self.produits.pop(j)
            # else:
            #     self.produits[j].quantite_en_stock += self.produits[i].quantite_en_stock
            #     self.produits.pop(i)

    def fusionerDouble(self):
        print("fusionner des produits doubles...")
        for i in range(len(self.produits)):
            for j in range(i+1, len(self.produits)-1):
                if self.produits[i].nom == self.produits[j].nom:
                    if self.produits[i].quantite_en_stock > self.produits[j].quantite_en_stock:
                        self.produits[i].quantite_en_stock += self.produits[j].quantite_en_stock
                        self.produits.pop(j)
                    else:
                        self.produits[j].quantite_en_stock += self.produits[i].quantite_en_stock
                        self.produits.pop(i)
                    print("operation finie")

    def chercherParMotCle(self, listed, motCle):
        for i in listed:
            if motCle.lower() in i.nom.lower():
                print(i.afficher())
