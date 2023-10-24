#Counting occurrences

#Write an algorithm that counts how many times a given element appears in an array.


taille=element=i=0
t=[30,20,4,6,7,20,6,5,8,1,20,3,6,7,9]
combien = 0
element=88

for i in range(len(t)):
    if t[i] ==element:
        combien+=1

print("combien de fois un élément donné apparaît dans un tableau est : ",combien)