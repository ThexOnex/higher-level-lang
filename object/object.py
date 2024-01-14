class Voiture:
    mat: str
    prix: float
    mark: str


lv = []


def ajouterVoiture():
    x = Voiture()
    x.mat = input("entrer la matricule : ")
    x.mark = input("entrer la mark : ")
    x.prix = float(input("entrer le prix : "))
    lv.append(x)
    print("Voiture ajouter avec succees")


def affichVoiture():
    for i in range(len(lv)):
        print("matricule: ", lv[i].mat, " La mark: ",
              lv[i].mark, " Le prix: ", lv[i].prix)


def chercher(mt):
    for i in range(len(lv)):
        if mt == lv[i].mat:
            return i
    return -1


def modifierPrix():
    mt = input("Entrer la matricule de la voiture a modifier ")
    rs = chercher(mt)
    if rs == -1:
        print("Voiture n'existe pas")
    prix = float(input("Entrer la nouveau prix"))
    lv[rs].prix = prix
    print("modifier avec succee")


def trierParPrix():
    for i in range(len(lv)-1):
        for j in range(i+1, len(lv)):
            if lv[i].prix > lv[j].prix:
                temp = lv[i]
                lv[i] = lv[j]
                lv[j] = temp


def trierParMark():
    for i in range(len(lv)-1):
        for j in range(i+1, len(lv)):
            if lv[i].mark > lv[j].mark:
                temp = lv[i]
                lv[i] = lv[j]
                lv[j] = temp


def surprime():
    taille = 0
    global lv
    mt = input("Entrer la matricule de la voiture a suprimer ")
    rs = chercher(mt)
    if rs == -1:
        print("Voiture n'existe pas")
    else:
        for i in range(rs, len(lv)-1):
            lv[i] = lv[i+1]
        taille = len(lv)-1
        lv = lv[::taille]
        print("voiture surprimer avec succee")
# appel


ajouterVoiture()
ajouterVoiture()
ajouterVoiture()
affichVoiture()
# modifierPrix()
# trierParPrix()
# trierParMark()
surprime()
affichVoiture()

# m = input("Tp la mat a chercher ")
# rs = chercher(m)
# if rs == -1:
#     print("La voiture n'existe pas")
# else:
#     print("La voiture exist a la position ", rs)

# appel
# v = Voiture()
# v1 = Voiture()
# v.mat = input("entrer la matricule : ")
# v.mark = input("entrer la mark : ")
# v.prix = float(input("entrer le prix : "))

# v1.mat = input("entrer la matricule : ")
# v1.mark = input("entrer la mark : ")
# v1.prix = float(input("entrer le prix : "))

# # affich
# print("matricule: ", v.mat, " La mark: ", v.mark, " Le prix: ", v.prix)
# print("matricule: ", v1.mat, " La mark: ", v1.mark, " Le prix: ", v1.prix)
