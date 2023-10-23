
note = add = 0
taille = int(input("Taper la nbr des notes : "))
t = [0] * taille

for i in range(taille):
    t[i] = float(input("entrer la note "))
    add = t[i] + add

print(t)
moy = add/taille
print(moy)
