class Personne:
    nom: str
    prenom: str
    genre: str
    conjoint: None

    def __init__(self, n, p, j):
        self.nom = n
        self.prenom = p
        self.genre = j
        self.conjoint = None

    def __str__(self):
        info = self.prenom, " ", self.nom, " ", self.genre
        if self.conjoint == None:
            return info, "est celibataire"
        return info, "est marrier avec", self.conjoint.nom, " ", self.conjoint.prenom, " ", self.conjoint.genre

    def tazawajBi(self, c):
        if self.genre == c.genre:
            print("siro l US :(")
        else:
            if self.conjoint != None or c.conjoint != None:
                print("chi 7ed fikom deja mzwej")
            else:
                self.conjoint = c
                c.conjoint = self
                print("Congrats")

    def tatala9aMin(self, c):
        if self.conjoint == None or c.conjoint == None:
            print("sir tzwej 3ad ji tle9")
        if self.conjoint == c and c.conjoint == self:
            self.conjoint = None
            c.conjoint = None
            print("Bon chance")
