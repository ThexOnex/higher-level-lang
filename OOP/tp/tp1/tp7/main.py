from employer import Employer
from pointage import Pointage
from gestion import GestionPointage

emp1 = Employer("m 1", "nom 1 ", "prenom 1", "11:30")
emp2 = Employer("m2", "n2", "p2", "10:25")
emp3 = Employer("m3", "n3", "p3", "13:33")
emp4 = Employer("m4", "n4", "p4", "8:20")

p1 = Pointage(2023, 2, 4, "12:30", "18:40", emp1)
p2 = Pointage(2023, 2, 4, "10:30", "17:30", emp2)
p3 = Pointage(2023, 2, 4, "8:30", "15:30", emp3)
p4 = Pointage(2023, 2, 4, "12:07", "17:20", emp4)

g = GestionPointage([p1, p2, p4])
# g.afficher_list_demployer()
# g.ajouterUnpointage(p3)
# g.afficher_list_demployer()
# how can i use the method afficher_details if the class is abstracted?????????????????
list_Polymorphique = [emp1, emp2, emp3, emp4, p1, p2, p3, p4]
# for i in list_Polymorphique:  # afficher tous des details
#     i.afficher_details()
# print("les heurs de travaille", p1.calculerLesHeursTravail())
# p3.calculerLesHeursTravail()
# print(g.chargerUneList())
# print(p1.calculerLesHeursTravail())
# print(p2.calculerLesHeursTravail())
# print(p4.calculerLesHeursTravail())

# print("total des heurs travailler par jour: ", g.nombreTotalTravailParJour())
# print("moyen d'heurs travaille par jour: ", g.moyenHeurTravailleParJour())
print("employe avec la plus grande work hours: ",
      g.employerAvecPlusGrandeHrurs())
