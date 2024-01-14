# Exercice 3: Modélisation d'une entreprise

# Créez une classe Employe avec les attributs suivants : nom, poste et salaire.

# Ajoutez une méthode augmenter_salaire à la classe Employe qui prend en paramètre un pourcentage d'augmentation et ajuste le salaire en conséquence.

# Créez une classe Departement avec les attributs suivants : nom et une liste d'employés.

# Ajoutez une méthode ajouter_employe à la classe Departement qui prend un objet Employe en paramètre et l'ajoute à la liste d'employés du département.

# Ajoutez une méthode afficher_employes à la classe Departement qui affiche les détails (nom, poste, salaire) de tous les employés du département.

# Créez une classe Entreprise avec les attributs suivants : nom et une liste de départements.

# Ajoutez une méthode ajouter_departement à la classe Entreprise qui prend un objet Departement en paramètre et l'ajoute à la liste de départements de l'entreprise.

# Ajoutez une méthode afficher_departements à la classe Entreprise qui affiche les noms de tous les départements de l'entreprise ainsi que les détails de leurs employés.

# Créez quelques instances de la classe Employe, Departement et Entreprise pour tester votre implémentation.
class Employ:
    nom: str
    poste: str
    salaire: float

    def __init__(self, n, p, s):
        self.nom = n
        self.poste = p
        self.salaire = s

    def augmenter_salaire(self, per):
        self.salaire += (self.salaire * (per/100))


class Departement:
    def __init__(self, n, e):
        self.nom = n
        self.employes = e

    def ajouter_employe(self, Employ):
        self.employes.append(Employ)

    def afficher_employes(self):
        for e in self.employes:
            print(f"nom: {e.nom} poste: {e.poste} salaire: {e.salaire}")


class Entreprise:
    def __init__(self, n, dep):
        self.nom = n
        self.departement = dep

    def ajouter_departement(self, Departement):
        self.departement.append(Departement)

    def afficher_departements(self):
        for d in self.departement:
            print(
                f"nom de departement: {d.nom}")
            d.afficher_employes()


em1 = Employ("nom1", "post1", 8000.0)
em2 = Employ("nom2", "post2", 5000.0)
em3 = Employ("nom3", "post3", 10000.0)
em4 = Employ("nom4", "post4", 6000.0)
liste = [em1, em2]
liste1 = [em3, em4]
dep1 = Departement("marketing", liste)
dep2 = Departement("sales", liste1)
dep3 = Departement("tech", [em1, em3])
Ent = Entreprise("name of company", [dep1, dep2])
dep1.ajouter_employe(Employ("nom3", "post3", 3000.0))
dep1.afficher_employes()
Ent.ajouter_departement(dep3)
Ent.afficher_departements()
