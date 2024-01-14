from produit import Produit
from pan import Panier

p1 = Produit("p1", 223, 10)
p2 = Produit("p2", 566, 2)
p3 = Produit("p3", 726, 5)
p4 = Produit("p4", 133, 4)

stacked = Panier([p1, p2, p3])
# stacked.ajouterProduct(p4)
# stacked.afficherProducts()
# print(stacked.calculerTotalProduits())
stacked.passerCommande()
