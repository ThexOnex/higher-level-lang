max = min = nbr = nbr2 = number = 0
taille = 0
taille = int(input("nomber des nbr "))
t = [0] * taille

nbr = int(input("Entrer la premiere nbr "))
max = min = nbr
t[0] = nbr

#if taille > 1:
   # nbr2 = int(input("Entrer 2nd nbr "))
  #  t[1] = nbr2
   # if nbr2<nbr:
   #     min = nbr2
   # else:
    #    min = nbr
   #     max = nbr2


for i in range(1,taille):
    nbr = int(input("nbr suivantes: "))
    t[i] = nbr
    if nbr > max :
        max = nbr
    elif nbr < min:
        min = nbr

print(t)
print("max est ",max,"min est ",min)

