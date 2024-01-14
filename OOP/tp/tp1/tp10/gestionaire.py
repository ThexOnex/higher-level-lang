from tachproblem import TacheInexistante
from invalidage import AgeInvalide
from invaliddate import ValueError
from invalidemail import ValidationError
from filefound import FileNotFoundError
from perm import PermissionError
import datetime
import os


class GestionnaireTaches:
    def __init__(self, l: list) -> None:
        self.taches = l

    def ajoutertache(self, t):
        self.taches.append(t)

    def markFinish(self, tch):
        try:
            if tch in self.taches:
                tch.etat = "terminée"
            else:
                raise TacheInexistante()
        except Exception as m:
            print(m)

    def afficherTch(self):
        for i in self.taches:
            i.afficher()

    def saisir_age(self):
        try:

            age = int(input("Entrer votre age: "))
            if age <= 0:
                raise AgeInvalide()
            else:
                print("l'age de l'utilisateur: ", age)
        except Exception as n:
            print(n)

    def convertir_date(self, chaine):
        try:
            tab = chaine.split("-")
            year = int(tab[0])
            # 1 or 2 digits for month
            month = int(tab[1])
            day = int(tab[2])
            if year > 2023 or month > 12 or day > 31 or len(tab) > 3:
                raise ValueError()
            date = datetime.date(year, month, day)
            return date
        except Exception as d:
            print(d)

    def valider_email(self, email):
        try:
            aro = 0
            point = 0
            for i in range(len(email)):
                if '@' == email[i]:
                    aro += 1
                if '.' == email[i]:
                    point += 1
                    if email[i+1] != 'c':
                        raise ValidationError()
            if aro != 1 and point != 1:
                raise ValidationError()
            else:
                print("valid email", email)

        except Exception as e:
            print(e)

    def copier_contenu(self, file1, file2):
        try:
            if not os.path.exists("c://"+file1) or not os.path.exists("c://"+file2):
                raise FileNotFoundError()
            # for excute it's X_OK
            if not os.access("c://"+file2, os.W_OK):
                raise PermissionError()
            f = open("c://"+file1, "r")
            file = f.read()
            lines = file.split("\n")
            f2 = open("c://"+file2, "a")
            for i in lines:
                f2.write("\n")
                f2.write(i)
            f2.close()
        except Exception as f:
            print(f)
