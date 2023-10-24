#Search in a table

#Write an algorithm that searches for a given element in an array and
#returns the index of the first occurrence of that element. If the element is not found, return -1.

taille = i = 0
t = [1,2,3,2,5,6,30,20]
element = int(input("on recherche l'element : "))
found = False
taille=len(t)
position = -1
for i in range(taille):
    if t[i] == element:
        position = i
        break
    i+=1

print("position est ",position)

