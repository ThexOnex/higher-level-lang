L=[3,2,4,5,6,1]

print("|pour ajouter un nombre taper ------------ 1                  |")
print("|pour chercher si le nombre exite taper ------------ 2       |")
print("|pour surprimer un nombre taper ------------ 3                |")
print("|pour trier le tableau en ordre croissant taper ------------ 4|")
print("|pour modifier un nombre dans ce position taper ------------ 5|")
i = int(input(": "))

if i == 1:
    v = int(input("entrer le nombre : "))
    taille = len(L)+1
    L1 = [0]*taille
    for i in range(taille-1):
        L1[i] = L[i]
    L1[taille-1] =v
    #L.append(v)
    print(L1)
elif i==2:
    bol = False
    v=int(input("entrer le nombre : "))
    for i in range(len(L)):
        if L[i]==v :
            bol = True
    # L.count(v)
    if bol == 0:
        print("le nombre n'exist pas ")
    else:
        print("le nombre exist dans le tableau ")
elif i==3:
    v=int(input("entrer le nombre : "))
    taille=len(L)-1
    for i in range(len(L)):
        if L[i] == v:
            pos = i
            break
    for i in range(pos,taille):
        L[i] = L[i+1]
    
    L=L[:taille]
    print(L)
elif i==4:
    temp = 0
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp

    print(L)
elif i==5:
    v =int(input("entrer la position de nbr "))
    n =int(input("entrer la nbr "))
    L[v] = n
    #L.insert(v,n)
    print(L)
else:
    print("erreur")