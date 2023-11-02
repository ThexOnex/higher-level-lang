L=["Sara",4,6,"lala","lol",3,0,3,'A']

print("|pour ajouter un element taper ------------ 1                  |")
print("|pour chercher si le nombre exite taper ------------ 2         |")
print("|pour surprimer un element taper ------------ 3                |")
print("|pour trier le tableau en ordre croissant taper ------------ 4 |")
print("|pour modifier un element dans ce position taper ------------ 5|")
i = int(input(": "))
tai1=tai2=v=0
bol = False

if i==1:
    while(bol ==False):
        answer=input("entrer yes si l'element est un nbr sinon no : ")
        if answer == 'yes':
            v = int(input("entrer l'element : "))
            bol=True
        elif answer=='no':
            v = input("entrer l'element : ")
            bol = True
        else:
            print("yes ou no seulement ")
    L.append(v)
    print(L)
elif i==2:
    while(bol ==False):
        answer=input("entrer yes si l'element est un nbr sinon no : ")
        if answer == 'yes':
            v = int(input("entrer l'element : "))
            bol=True
        elif answer=='no':
            v = input("entrer l'element : ")
            bol = True
        else:
            print("yes ou no seulement ")
    L.count(v)
    if L.count(v) == 0:
        print("l'element n'exist pas ")
    else:
        print("l'element exist dans le tableau ")
elif i==3:
    while(bol ==False):
        answer=input("entrer yes si l'element est un nbr sinon no : ")
        if answer == 'yes':
            v = int(input("entrer l'element : "))
            bol=True
        elif answer=='no':
            v = input("entrer l'element : ")
            bol = True
        else:
            print("yes ou no seulement ")
    if L.count(v) == 1:
        L.remove(v)
        print(L)
    else:
        print("taper l'element une autre fois ")
elif i==4:
    t1=[]
    t2=[]
    for i in range(len(L)):
        if isinstance(L[i],int):
            t1.append(L[i])
        elif isinstance(L[i],str):
            t2.append(L[i])
    t1.sort()
    t2.sort()
    print(t1)
    print(t2)
elif i == 5:
    while(bol ==False):
        v =int(input("entrer la position de nbr "))
        if v < len(L):
            bol = True
        else:
            print("la position doit etre entre 0 et ",len(L))
    bol = False
    while(bol ==False):
        answer=input("entrer yes si l'element est un nbr sinon no : ")
        if answer == 'yes':
            n = int(input("entrer l'element : "))
            bol=True
        elif answer=='no':
            n = input("entrer l'element : ")
            bol = True
        else:
            print("yes ou no seulement ")
    L[v] = n
    #L.insert(v,n)
    print(L)
else:
    print("erreur")