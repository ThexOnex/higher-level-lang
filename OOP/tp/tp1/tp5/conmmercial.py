from person import Person
import datetime


class Commercaile(Person):
    def __init__(self, n, p, g, a, m, j, pr: float, s: float, c: str):
        super().__init__(n, p, g)
        self.date_of_hire = datetime.date(a, m, j)
        self.prime = pr
        self.salaire_de_base = s
        self.cin = c

    def __str__(self) -> str:
        return super().__str__() + f"date of hire {self.date_of_hire} prime: {self.prime} salaire de base: {self.salaire_de_base} Cin: {self.cin}"

    def calculerEnciente(self):
        string = str(datetime.date.today() - self.date_of_hire)
        time = string.split(" ")
        date = int(time[0]) / 365.25
        return date

    def calculerSalaire(self):
        salary = self.salaire_de_base + self.prime

        if self.calculerEnciente() < 5:
            return salary
        elif self.calculerEnciente() >= 5 and self.calculerEnciente() < 10:
            return salary + (self.salaire_de_base * 0.1)
        elif self.calculerEnciente() >= 10:
            return salary + (self.salaire_de_base * 0.2)
