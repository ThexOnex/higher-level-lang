L=[10,5,2,6,37,8,2,4]

print("|pour ajouter un nombre taper ------------ 1                  |")
print("|pour chercher si le nombre exite taper ------------ 2       |")
print("|pour surprimer un nombre taper ------------ 3                |")
print("|pour trier le tableau en ordre croissant taper ------------ 4|")
print("|pour modifier un nombre dans ce position taper ------------ 5|")
i = int(input(": "))

if i == 1:
    v = int(input("entrer le nombre : "))
    L.append(v)
    print(L)
elif i==2:
    v=int(input("entrer le nombre : "))
    L.count(v)
    if L.count(v) == 0:
        print("le nombre n'exist pas ")
    else:
        print("le nombre exist dans le tableau ")
elif i==3:
    v=int(input("entrer le nombre : "))
    if L.count(v) == 0:
        print("le nombre n'exist pas taper le nbr une autre fois")
    else:
        L.remove(v)
        print(L)
elif i==4:
    L.sort()
    print(L)
elif i==5:
    v =int(input("entrer la position de nbr "))
    n =int(input("entrer la nbr "))
    L[v] = n
    #L.insert(v,n)
    print(L)
else:
    print("erreur")