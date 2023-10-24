#reverse an array
t=[1,2,3,4,5]
temp = 0
taille = int(len(t)/2)

for i in range(taille):
    temp = t[i]
    t[i] = t[(len(t)-1)-i]
    t[(len(t)-1)-i] = temp

print(t)