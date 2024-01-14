# Gestion d'une bibliothèque

# Créez une classe appelée Livre avec les attributs suivants : titre, auteur, année et disponible (un booléen indiquant si le livre est disponible ou non).

# Ajoutez une méthode emprunter à la classe Livre qui change l'état de disponibilité à False lorsque le livre est emprunté.

# Ajoutez une méthode retourner à la classe Livre qui change l'état de disponibilité à True lorsque le livre est retourné.

# Créez une classe appelée Bibliotheque qui contient une liste de livres.

# Ajoutez une méthode à la classe Bibliotheque pour afficher tous les livres disponibles.

# Créez quelques instances de la classe Livre et ajoutez-les à la bibliothèque.

# Affichez la liste des livres disponibles.

# Empruntez un livre, puis affichez à nouveau la liste des livres disponibles pour vérifier que le livre emprunté n'est plus dans la liste.
class Livre:
    titre: str
    auteur: str
    annee: int
    disponible: bool

    def __init__(self, T, A, AN, D):
        self.titre = T
        self.auteur = A
        self.annee = AN
        self.disponible = D

    def emprunter(self):
        self.disponible = False

    def retourner(self):
        self.disponible = True


class Bibliotheque:
    def __init__(self, livre):
        self.livres = livre

    def affich(self):
        for i in range(len(self.livres)):
            if self.livres[i].disponible:
                print(self.livres[i].titre)


livre1 = Livre("titre1", "auteur1", 2006, True)
livre2 = Livre("titre2", "auteur2", 2002, True)
livre3 = Livre("titre3", "auteur3", 2016, True)
livre4 = Livre("titre4", "auteur4", 2005, True)
listl = [livre1, livre2, livre3, livre4]
bib = Bibliotheque(listl)
bib.affich()
livre2.emprunter()
bib.affich()
