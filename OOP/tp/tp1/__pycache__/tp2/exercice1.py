# **Exercice 1 : Gestion d'une entreprise**

# Considérez une entreprise qui a différents types d'employés, tels que les employés réguliers, les gestionnaires et les directeurs. Chaque type d'employé a des attributs et des comportements spécifiques.

# 1. **Création des classes de base :**
#    - Définissez une classe de base appelée `Employe` avec les attributs communs tels que le nom, le numéro d'employé et le salaire de base.
#    - Ajoutez une méthode `calculer_salaire` qui renvoie le salaire de base.

# 2. **Classes dérivées :**
#    - Créez deux classes dérivées, `Manager` et `Directeur`, qui héritent de la classe `Employe`.
#    - Ajoutez des attributs spécifiques à chaque classe, par exemple, pour le `Manager`, ajoutez une prime de gestion, et pour le `Directeur`, ajoutez une prime de direction.
#    - Surchargez la méthode `calculer_salaire` dans chaque classe dérivée pour prendre en compte les attributs spécifiques.

# 3. **Employé régulier :**
#    - Ajoutez une classe dérivée `EmployeRegulier` qui hérite de la classe `Employe`.
#    - Intégrez des attributs tels que les heures travaillées et le taux horaire.
#    - Surchargez la méthode `calculer_salaire` pour prendre en compte le salaire en fonction des heures travaillées.

# 4. **Gestion des promotions :**
#    - Ajoutez une méthode `promouvoir` à la classe de base `Employe`, qui permet de promouvoir un employé à un niveau supérieur (par exemple, d'EmployeRegulier à Manager).
#    - Assurez-vous que la méthode ajuste correctement les attributs et comportements en fonction du type de promotion.

# 5. **Test du système :**
#    - Créez quelques instances d'employés, de managers et de directeurs.
#    - Effectuez des opérations telles que le calcul du salaire, la promotion d'employés, etc.
#    - Affichez les résultats pour vérifier que votre système de gestion d'entreprise fonctionne correctement.
class Employe:
    nom: str
    numero: int
    salaireBase: float

    def __init__(self, name, number, salary):
        self.nom = name
        self.numero = number
        self.salaireBase = salary

    def __str__(self):
        return f"name: {self.nom} number: {self.numero} salary: {self.salaireBase}"

    def calculer_salaire(self):
        return self.salaireBase

    def promouvoir(self, newClasse, **kwargs):
        if isinstance(self, newClasse):
            return f"{self.nom} est déjà {newClasse.__name__}"

        nouveau_poste = newClasse(**kwargs)
        return f"{self.nom} a été promu(e) à {newClasse.__name__}"


class Manager(Employe):
    primeGestion: float

    def __init__(self, name, number, salary, managerBonus):
        super().__init__(name, number, salary)
        self.primeGestion = managerBonus

    def calculer_salaire(self):
        return super().calculer_salaire() + self.primeGestion


class Directeur(Employe):
    primeDirection: float

    def __init__(self, name, number, salary, directorBonus):
        super().__init__(name, number, salary)
        self.primeDirection = directorBonus

    def calculer_salaire(self):
        return super().calculer_salaire() + self.primeDirection


class EmployeRegulier(Employe):
    workHour: float
    hourRate: float

    def __init__(self, name, number, salary, wh, hr):
        super().__init__(name, number, salary)
        self.hourRate = hr
        self.workHour = wh

    def calculer_salaire(self):
        return self.workHour * self.hourRate * 4


employe1 = Employe("name em", 6766, 5464)
employe2 = Employe("name em2", 6886, 7464)
employe3 = EmployeRegulier("name em3", 8866, 3464, 4, 7)
employe4 = EmployeRegulier("name em4", 6799, 5464, 6, 5)

dir1 = Directeur("name dr1", 2222, 10456, 1000)
dir2 = Directeur("name dr2", 77777, 9956, 1000)

mg1 = Manager("name mg1", 7334, 9283, 1200)
mg2 = Manager("name mg2", 7334, 10283, 1000)

print(dir2.calculer_salaire())
print(employe3.promouvoir(Manager, name="name mg3",
      number=5464, salary=10000, managerBonus=1200))
employe3.promouvoir(Manager, name="name mg3",
                    number=5464, salary=10000, managerBonus=1200)
print(employe3.__str__())
