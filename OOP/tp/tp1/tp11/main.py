from etudiant import Etudiant
from ens import Enseignant
from cont import Contreleur
from file import GestionEducationFichier
from cour import Cours
et1 = Etudiant("nom", "prenom", 15, [17, 20, 18, 16])
et2 = Etudiant("nom2", "prenom2", 16, [7, 10, 13, 9.5])
et3 = Etudiant("nom3", "prenom3", 18, [10, 12, 16, 12.5])

en1 = Enseignant("nom en 1", "pre en 1", 16, "matieres enseignees 1")
en2 = Enseignant("nom en 2", "pre en 2", 20, "matieres_enseignees 2")
en3 = Enseignant("nom en 3", "pre en 3", 18, "matieres_enseignees 3")

c1 = Cours("HTML", en1, True)
c2 = Cours("Python", en2, True)
c3 = Cours("CSS", en3, False)

# c1.afficherDetails()
educateur = [en1, en2, en3]
people = [et1, et2, et3, en1, en2, en3]
etudiant = [et1, et2, et3]

plat = Contreleur(etudiant)
file = GestionEducationFichier(people)
