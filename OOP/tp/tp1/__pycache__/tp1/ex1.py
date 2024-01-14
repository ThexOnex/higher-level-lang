# Exercice 1: Création d'une classe "Rectangle"

# Créez une classe appelée Rectangle.
# Ajoutez un constructeur à la classe Rectangle qui prend la longueur et la largeur comme paramètres et initialise les attributs correspondants.
# Ajoutez des méthodes à la classe Rectangle pour calculer la superficie et le périmètre du rectangle.
# Créez deux instances de la classe Rectangle avec différentes dimensions.
# Affichez la superficie et le périmètre de chaque rectangle.

class Rectangle:
    length: float
    width: float

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def superficie(self):
        return (self.length * self.width)

    def perimetre(self):
        return (2 * (self.length + self.width))


rec1 = Rectangle(5, 8)
rec2 = Rectangle(7, 9)
print("la superficie de la premire rectangle est: ",
      rec1.superficie(), " et le périmètre: ", rec1.perimetre())
print("la superficie de la deuxieme rectangle est: ",
      rec2.superficie(), " et le périmètre: ", rec2.perimetre())
