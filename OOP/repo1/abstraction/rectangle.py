from formGeo import FormGeometrique


class Rectangle(FormGeometrique):
    largeur: float
    longeur: float

    def __init__(self, l, ln):
        self.largeur = l
        self.longeur = ln

    def afficher(self):
        print(f"la surface est: {self.calculerSurface()}")

    def calculerSurface(self):
        return self.largeur * self.longeur
