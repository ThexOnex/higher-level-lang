from employer import Employer
from conmmercial import Commercaile
from conge import Conge
from construct import Contreleur
emp1 = Employer("Hachir", "Ahmad", "M", 2020, 6, 8, 100, 5000, "EE345")
emp2 = Employer("Hachir2", "Ahmad2", "M", 2018, 2, 19, 200, 4000, "EE7685")
com1 = Commercaile("blabla", "nom 1", "F", 2019, 9, 5, 1000, 6000, "EE695")
com2 = Commercaile("blabla2", "nom 2", "M", 2021, 9, 10, 1500, 8000, "EE777")

conge1 = Conge("id conge", 2023, 5, 10, 2023, 5, 25)
conge2 = Conge("id conge 2", 2023, 1, 1, 2023, 1, 25)
# print(emp1.calculerEnciente())
# print("the salary of the employer: ", emp1.calculerSalaire())
# # explicite : type var valeur
# print(com1.calculerEnciente())
# print(com1.calculerSalaire())
# print("number of days in work holiday: ", conge1.calculerNombreDeJour())
c = Contreleur([emp1, emp2, com1, com2], [conge1])
c.ajouterConge(conge2)
# print(conge2.calculerNombreDeJour())
c.sauvegarderDansUnFishier()
# c.modifierPerson(1)
# c.afficherEmployers()
# c.chercherParCin("EE345")
# c.trieeParDate()
# c.afficherEmployers()
# c.afficherEmployers()
# com3 = Commercaile("blabla3", "nom 3", "M", 2022, 5, 20, 2000, 7000, "EE885")
# c.ajouterPersonne(com3)
# print("=============================================")
# c.afficherEmployers()
# print("=============================================")
# c.surprimerPerson(com1)
# c.afficherEmployers()
