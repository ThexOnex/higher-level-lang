from vol import Vol
from GestionAeroport import GestionAeroport
from passage import Passager
from VolInternational import VolInternational
from VolNational import VolNational
from GestiontFichier import GestionAeroportFichier
voln1 = VolNational(4364, "compagne 1", 13, 22, "A-01", "Los Angelos")
voln2 = VolNational(4774, "compagne 1", 15, 23, "A-02", "LA")
voln3 = VolNational(8368, "compagne 1", 17, 12, "A-03", "TEXAS")

voli1 = VolInternational(5555, "compagne inte1", 14, 19, "B-01", "Morocco")
voli2 = VolInternational(5665, "compagne inte2", 11, 22, "B-01", "Algeria")
voli3 = VolInternational(5994, "compagne inte3", 15, 20, "B-01", "Egypt")

pas1 = Passager("nom passage 1", "prenom passage 1", 72939, "eco")
pas2 = Passager("nom passage 2", "prenom passage 2", 73444, "affaire")
pas3 = Passager("nom passage 3", "prenom passage 3", 555544, "business")

gestion = GestionAeroport([voli1, voln1, voln2, voln3, voli3])
fishier = GestionAeroportFichier(
    [voli1, voli2, voli3, voln1, voln2, voln3], [])

# fishier.sauvgarder()
# print(voli1.__str__())

fishier.charger()
fishier.afficherLesCHarger()

# gestion.afficherDesVols()
# print("=============================================================================")
# gestion.trieParheure()
# gestion.ajouterUnVol(voli2)
# gestion.afficherDesVols()
# gestion.retirerUnVol(voli2)
# gestion.afficherDesVols()
