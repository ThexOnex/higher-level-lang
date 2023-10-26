print("================================================================")
print("---------------------------BIENVENU-----------------------------")
print("   mark                                        prix par jour    ")
print("   Dacia                                          234dh         ")
print("   Audi                                           260dh         ")
print("   Ford                                           300dh         ")
print("----------------------------------------------------------------")
print("================================================================")
mark=['Dacia','Audi','Ford']
prix=[234,260,300]

d={'mark':mark,'prix':prix}
numdays=[]
bol =stop=False
days=total=index=price=0
answer=""
d1={}

while(stop==False):
    price=0
    while(bol == False):
        mark1 = input("Entrer la mark ")
        if mark1==mark[0]:
            print("le prix est",prix[0])
            price+=prix[0]
            d1[mark[0]]=prix[0]
            break
        elif mark1==mark[1]:
            print("le prix est",prix[1])
            price+=prix[1]
            d1[mark[1]]=prix[1]
            break
        elif mark1==mark[2]:
            print("le prix est",prix[2])
            price+=prix[2]
            d1[mark[2]]=prix[2]
            break
        else:
            print("On n'a pas trouver la mark")
            continue

    days=int(input("pour combien de jours veux-tu cette voiture? "))
    numdays.append(days)

    total = (days*price)+total
    price=0
    while(bol==False):
        answer=input("voulez-vous une autre voiture ? ")
        if answer== 'oui':
            break
        elif answer== 'no':
            stop =True
            break
        else:
            print("Taper oui ou no")
            continue
i = 0
print("=========================================================")
print("--------------------------FACTURE------------------------")
print("   les mark               le prix          nombre de jour")
for x,y in d1.items():
    print("   ",x,"                 ",y,"dh",end='')
    print("          ",numdays[i])
    i+=1
print("---------------------------------------------------------")
print("total -------------------------------------------",total,"dh")
print("=========================================================")

