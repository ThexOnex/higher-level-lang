def charge(t):
    i = 0
    for i in range(len(t)):
        t[i] = int(input("Entrer un nbr "))
    return t


def affich(t):
    i = 0
    for i in range(len(t)):
        print(t[i])


def _index(t, n):
    i = 0
    for i in range(len(t)):
        if t[i] == n:
            return i
    return -1


def surp(t, n):
    taille = len(t)
    i = 0
    for i in range(n, len(t)-1):
        t[i] = t[i+1]
    taille1 = taille - 1
    t = t[:taille1]
    return t


def mod(t, n, m):
    i = 0
    for i in range(len(t)):
        if t[i] == n:
            t[i] = m
            return 0
    return -1


def tri(t):
    i = 0
    temp = 0
    for i in range((len(t))):
        for j in range(len(t)-1):
            if t[j] > t[j+1]:
                temp = t[j]
                t[j] = t[j+1]
                t[j+1] = temp
    return t


def reversed(t):  # 1 2 3 4   4 3 2 1
    temp = 0
    for i in range(int(len(t)/2)):
        temp = t[i]
        t[i] = t[len(t)-1-i]
        t[len(t)-1-i] = temp
    return t


t = []
stop = yes = False

while (stop == False):
    yes = False
    print("------------------------", t, "---------------------------")
    print("pour charger le tableau Taper 1")
    print("pour affich les elements du tableau Taper 2")
    print("pour chercher dans le tableau Taper 3")
    print("pour surprimer un element dans le tableau Taper 4")
    print("pour modifer un element dans le tableau Taper 5")
    print("pour trier le tableau Taper 6")
    choice = int(input("votre choix est : "))
    if choice == 1:
        taille = 0
        taille = int(input("entrer la taille de tableau : "))
        t = [0]*taille
        print(charge(t))
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue
    elif choice == 2:
        affich(t)
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue
    elif choice == 3:
        nombre = int(input("Entrer le nombre : "))
        if _index(t, nombre) == -1:
            print("ce nombre n'exist pas dans ce tableau")
        else:
            print("la position de ce nombre est : ", _index(t, nombre))
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue
    elif choice == 4:
        nombre = int(
            input("Entrer la position d'element pour le surprimer : "))
        if nombre >= len(t):
            print("=================================Ce position n'existe pas (out of range)================================")
            continue
        print("avant: ", t)
        print("le tableau apres : ", surp(t, nombre))
        taille1 = taille - 1
        t = t[:taille1]
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue
    elif choice == 5:
        nombre = int(input("Entrer le nombre que vous voulez le changer: "))
        change = int(input("le nombre que vous voulez remplacer: "))
        print("avant: ", t)
        r = mod(t, nombre, change)
        if r == -1:
            print("Ce nombre n'exist pas")
        else:
            print(t)
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue
    elif choice == 6:
        print(tri(t))
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue
    elif choice == 7:
        reversed(t)
        print(t)
        while (yes == False):
            choice1 = input("voulez vous modifier une chose ? ")
            if choice1 == 'yes':
                break
            elif choice1 == 'no':
                stop = True
                break
            else:
                print("Taper yes ou no")
                continue

    else:
        print("========================Taper 1 ou 2 ou 3 ou 4 ou 5 ou 6======================================")
        print("===============================================================================================")
        continue
