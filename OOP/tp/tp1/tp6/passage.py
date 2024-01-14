class Passager:
    nom: str
    prenom: str
    numero_passeport: int
    classe: str

    def __init__(self, n, p, nu, c) -> None:
        self.nom = n
        self.prenom = p
        self.numero_passeport = nu
        self.classe = c

    def embarquement(self):
        print(self.nom, "a embarquer, le passport ",
              self.numero_passeport, " classe ", self.classe)

    def débarquement(self):
        print(self.nom, "a debarquer, passport: ",
              self.numero_passeport, " classe ", self.classe)
