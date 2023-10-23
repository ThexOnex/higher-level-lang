#Séparation des éléments pairs et impairs

#Écrivez un algorithme qui sépare les éléments pairs 
#des éléments impairs dans un tableau en deux tableaux distincts.


t = [1,2,3,4,5,6,7]
taille=taille1=taille2=0
taille =len(t)


for i in range(taille):
    if t[i]%2==0:
        taille1+=1
    else:
        taille2+=1

print(taille1)
print(taille2)
t1 = [0]*taille1
t2 = [0]*taille2
j=m=0
for i in range(taille):
    if t[i]%2==0:
        t1[j]=t[i]
        j+=1
    else:
        t2[m]=t[i]
        m+=1

print(t1,"pair")
print(t2,"impair")