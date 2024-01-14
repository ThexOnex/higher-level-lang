import datetime


class Emp:  # type is emp
    CIN: str
    NOM: str
    PRENOM: str
    SALAIRE: float
    date_amb:  datetime

    def __init__(self, C, N, P, S, A, M, J):
        self.CIN = C
        self.NOM = N
        self.PRENOM = P
        self.SALAIRE = S
        self.date_amb = datetime.date(A, M, J)

    def afficher(self):
        print(self.CIN, " ", self.NOM, " ", self.PRENOM,
              " ", self.SALAIRE, " ", self.date_amb)

    def __str__(self):
        return (self.CIN, " ", self.NOM, " ", self.PRENOM,
                " ", self.SALAIRE, " ", str(self.date_amb))

    def __eq__(self, obj):
        if self.CIN == obj.CIN:
            return True
        return False
