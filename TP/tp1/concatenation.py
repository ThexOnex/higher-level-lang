#Array concatenation

#Write an algorithm that takes two arrays
#as input and returns a third array which is the concatenation of the two arrays.
taille1 = taille2=taille3=j= 0
taille1 = int(input("entrer le nbr des element dans le 1er tableau "))
taille2 = int(input("entrer le nbr des element dans le 1er tableau "))

t1 = [0]*taille1
t2 = [0]*taille2

for i in range(taille1):
    print("tab 1 : la nombre du numero ",i)
    t1[i] = int(input(" est : "))

for i in range(taille2):
    print("tab 2 : la nombre du numero ",i)
    t2[i] = int(input(" est : "))

print(t1)
print(t2)
taille3= taille1+taille2
Tcon = [0]*taille3

for i in range(taille1):
    Tcon[i] = t1[i]

i=taille1
while(i<taille3):
    Tcon[i] = t2[j]
    j+=1
    i+=1


print(Tcon)


