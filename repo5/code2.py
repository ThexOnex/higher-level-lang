def charger(t):
    i = 0
    for i in range(len(t)):
        t[i] = int(input(" entrer : "))


def afficher(t):
    i = 0
    for i in range(len(t)):
        print(t[i])


def chercher(x, t):
    i = 0
    p = -1
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1


t = []
taille = 0
taille = int(input("entrer la taille"))
t = [0]*taille
charger(t)
afficher(t)
y = 0
y = int(input("taper l'element a chercher "))
r = chercher(y, t)
if r == -1:
    print("element n'existe pas")
else:
    print("l'element trouver sa position est : ", r)
