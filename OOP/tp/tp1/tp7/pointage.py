import datetime
from employer import Employer


class Pointage:
    date: datetime
    heure_arrivee: str
    heure_depart: str
    employe: Employer

    def __init__(self, y, m, d, h, hd, e) -> None:
        self.date = datetime.date(y, m, d)
        self.heure_arrivee = h
        self.heure_depart = hd
        self.employe = e

    def afficher_details(self):
        print(f"Date: {self.date}")
        print(f"Heure d'arrivée: {self.heure_arrivee}")
        print(f"Heure de départ: {self.heure_depart}")
        print(f"Employé: {self.employe.nom}")

    def calculerLesHeursTravail(self):
        lineOne = self.heure_arrivee.split(":")
        lineTwo = self.heure_depart.split(":")
        hourOne = int(lineOne[0])
        hourTwo = int(lineTwo[0])
        minuteOne = int(lineOne[1])
        minuteTwo = int(lineTwo[1])
        hours = hourTwo - hourOne
        minutes = minuteOne + minuteTwo
        if minutes >= 60:
            minutes -= 60
            hours += 1
        return str(hours) + ":" + str(minutes)
