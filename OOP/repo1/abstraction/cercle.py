from formGeo import FormGeometrique


class Cercle(FormGeometrique):
    rayon: float

    def __init__(self, s):
        self.rayon = s

    def __str__(self):
        return f"le rayon est : {self.rayon}"

    def calculerSurface(self):
        return self.rayon * self.rayon * 3.14

    def afficher(self):
        print(f"la surface du cercle est: {self.calculerSurface()}")
