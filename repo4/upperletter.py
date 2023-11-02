#convert any string into an string that has the first letter uppercase and the rest is lowercase


Mot = input("Entrer le mot :")
MJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MN = "abcdefghijklmnopqrstuvwxyz"
nm = ""
min = False

for i in range(len(MN)):
    if Mot[0] == MN[i]:
        nm += MJ[i]
        min = True
else:
    nm = nm + Mot[0]


for i in range(1,len(Mot)):
    for j in range(len(MJ)):#is maj
        if Mot[i] == MJ[j]:
            nm += MN[j]
            break
        # elif Mot[i]!=MJ[len(MJ)-1] and j == len(MJ)-1:#is min
        #     nm += Mot[i]
    else :
        nm+=Mot[i]

print(nm)


