# def multip(*a):
#     s = 0
#     for i in range(len(a)):
#         s += a[i]
#     return s


# print(multip(3, 4, 5, 7, 83, 5))
# examples 4

def charge(t):
    i = 0
    for i in range(len(t)):
        t[i] = int(input("Entrer un nbr "))
    return t


def affich(t):
    i = 0
    for i in range(len(t)):
        print(t[i])


t2 = []
taille = 0
taille = int(input("Entrer la taille : "))
t2 = [0]*taille

print(charge(t2))
affich(t2)
