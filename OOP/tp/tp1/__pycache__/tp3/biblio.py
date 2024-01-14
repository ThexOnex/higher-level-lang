from livre import Livre
from nonEmprunte import LivreEmpruntable


class Bibliotheque:
    def __init__(self):
        self.listMembres = []
        self.listLivres = []

    def ajouterLivre(self, obj):
        self.listLivres.append(obj)

    def surprimerLivre(self, livre):
        self.listLivres.remove(livre)

    def afficherLivresDisponible(self):
        for i in self.listLivres:
            if i.disponible:
                print(i, "est dispo")

    def rechercherLivre(self):
        choix = input(
            "Entrer 1 pour rechercher un livre par un titre ou un auteur, entrer 2 pour rechercher un livre par l'annee")
        if choix == '1':
            search = input("Entrer le titre ou auteur de livre: ")
            for i in self.listLivres:
                if search in i:
                    print("On a trouvee Ce livre: ", i)
        elif choix == '2':
            search = int(input("Entrer l'annee de livre: "))
            for i in self.listLivres:
                if str(search) in i:
                    print("On a trouvee Ce livre: ", i)
