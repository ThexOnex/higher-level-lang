# procedure

def bonsoir(mot):
    print("Bonsoir", mot)


def Concatenation(m1, s, m2):
    c = ""
    c = m1 + s + m2
    print(c)


def remplire(t1):
    # taille = 0
    # taille = int(input("Entrer la taille : "))
    # t = [0]*taille
    for i in range(len(t1)):
        t1[i] = int(input("Entrer un nombre "))
    print(t1)


def afficher(t):
    for i in range(len(t)):
        print(t[i])


def carre(a):
    c = 0
    c = a*a
    print(c)


# def afficher(tb):
#     for i in range(len(tb)):
#         print(tb[i])
def facto(a):

    for i in range(1, a):
        a *= i
    print(a)


def puiss(x, y):
    a = 1
    for i in range(y):
        a *= x
    print(a)


def validtel(n):
    num = "1234567890"
    bolNum = False
    if len(n) != 10:
        print("numero pas valider")
    else:
        for i in range(len(n)):
            for j in range(len(num)):
                if n[i] != num[i]:
                    bolNum = True
                    break
            else:
                bolNum == False
        if bolNum != True:
            print("valid")
        else:
            print("pas valid")


# appel

x = input("Entrer votre num de tel ")
validtel(x)
# m = input("Taper votre prenom ")
# bonsoir(m)

# a = input("Taper votre prenom ")
# b = input("Taper votre separateur ")
# c = input("Taper votre nom ")

# Concatenation(a, b, c)

# x = int(input("Taper un nbr "))
# y = int(input("Taper un nbr "))
# carre(x)
# facto(x)
# puiss(x, y)
# t1 = []
# taille = 0
# taille = int(input("La taille : "))
# t1 = [0]*taille

# remplire(t1)
# afficher(t1)
