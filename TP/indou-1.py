#Search in a table

#Write an algorithm that searches for a given element in an array and
#returns the index of the first occurrence of that element. If the element is not found, return -1.

taille = i = 0
t = [1,2,3,2,5,6,30,20]
element =30
found = False
taille=len(t)

while(i<taille and found==False):
    if t[i] ==element:
        found = True
    i+=1

if found == True:
    print("indice est ",i)
else:
    print("-1")