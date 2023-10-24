t = [7,3,11,1,15,10]
taille = len(t)
temp = 0
print(taille)

for i in range(taille-1):
    for j in range(i+1,taille):
        if t[i] > t[j]:
            temp = t[i]
            t[i] = t[j]
            t[j] = temp

print(t)