#Addition of tables
#Write an algorithm that takes two arrays as input and
#returns a third array that is the sum of the two input arrays (element by element).

t1=[1,2,3,4]
t2=[5,6,7,8]
taille1=taille2=0
taille1=len(t1)
taille2=len(t2)

if taille1==taille2:
    t3=[0] * taille2
    for i in range(taille1):
        t3[i]=t1[i]+t2[i]
    print("tableau 1 : ",t1)
    print("tableau 2 : ",t2)
    print("l'addition des 2 tableau : ",t3)
else:
    print("les tailles ne sont pas la meme")    