import datetime


class Conge:
    idConge: str
    dateDebut: datetime
    dateFin: datetime

    def __init__(self, i, a, m, j, y, mm, jj) -> None:
        self.idConge = i
        self.dateDebut = datetime.date(a, m, j)
        self.dateFin = datetime.date(y, mm, jj)

    def __str__(self) -> str:
        return f"Id of the work holiday: {self.idConge}, start date: {self.dateDebut}, finish date: {self.dateFin}"

    def calculerNombreDeJour(self):
        string = str(self.dateFin - self.dateDebut)
        time = string.split(" ")
        date = int(time[0])
        return date
