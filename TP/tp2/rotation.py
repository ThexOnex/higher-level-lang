#Circular rotation of a table
#Write an algorithm that circularly rotates an array to the left by a certain number of positions.
#For example, [1, 2, 3, 4, 5] rotated 2 positions should become [3, 4, 5, 1, 2]


t=[1,2,3,4,5]
move=taille=p=0
taille=len(t)
r=[0]*taille
p=3
for i in range(taille):
    if i-p<0:
        r[taille-p+i]=t[i]
    else:
        r[i-p]=t[i]

print(t)
print(r)