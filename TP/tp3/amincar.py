mark=['Dacia','Audi','Ford']
prix=[234,260,300]
d = {'mark':mark,'price':prix}

username = "Admin"
password = "123456"
AU=False
while (AU == False):
    choice = input("vous etes user ou un admin ? ")
    if choice == 'user':
        first =False
        AU = True
        while(first==False):
            print("=============================USER===============================")
            print("---------------------------BIENVENU-----------------------------")
            print("   mark                                        prix par jour    ")
            print("----------------------------------------------------------------")
            for x,y in d.items():
                print("   ",x,"                                      ",y,"dh")
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
            print("----------------------------------------------------------------")
            for x,y in d1.items():
                print("   ",x,"                 ",y,"dh",end='')
                print("          ",numdays[i])
                i+=1
            print("---------------------------------------------------------")
            print("total -------------------------------------------",total,"dh")
            print("=========================================================")
            print("----------|Modifier|-----------OU---------|quitter|------")
            print(d1)
            print("pour Modifier taper le mot 'modifier'pour quitter taper'quitter'")
            while(bol==False):
                answer1=input("")
                if answer1=='modifier':
                    break
                elif answer1=='quitter':
                    first=True
                    bol=True
                    break
                else:
                    print("incorrect")

    elif choice == 'admin':
        AU = True
        blocked=False
        print("Entrer le nom est mode de pass")
        for i in range(3):
            if i==2:
                print("C'est la derniere fois")
            test1=input("entrer username : ")
            test2=input("entrer mode de pass : ")
            if test1==username and test2==password:
                break
            else:
                print("incorrect")
                if i==2:
                    print("comnpte blocker")
                    blocked = True
            
        if blocked!= True :
            print("============================ADMIN===============================")
            print("---------------------------BIENVENU-----------------------------")
            print("   mark                                        prix par jour    ")
            print("----------------------------------------------------------------")
            for x in range(len(mark)):
                print("   ",mark[x],end='')
                print("                                        ",prix[x],"dh")
            print("----------------------------------------------------------------")
            print("================================================================")

            bol = False
            while(bol==False):
                choice = input("voulez-vous modifier le menu, si oui Taper oui ? ")
                if choice == 'oui':
                    print("pour ajouter une voiture Taper 1")
                    print("pour surprimer une voiture Taper 2")
                    print("pour modifier le prix Taper 3")
                    answer = input("votre choix est : ")
                    break
                elif choice == 'no':
                    break
                else : 
                    print("taper oui ou no")
                    continue
            if choice=='no':
                break
            if answer == '1':
                print(d)
                car = input("le nom de voiture : ")
                markd.append(car)
                pri = input("le prix de ce voiture : ")
                prix.append(pri)
                d[car]=pri
                print(d)
                print(mark)
                print(pri)
            elif answer == '2':
                print(d)
                car = input("le nom de voiture pour la surprimer : ")
                for i in range(len(mark)):
                    if car==mark[i]:
                        del d[mark[i]]
                        mark.remove(mark[i])
                        prix.remove(prix[i])
                        break
                print(d)
                print(mark)
                print(prix)
            elif answer == '3':
                car = input("entrer le voiture que vous voulez le changer le prix ")
                for i in range(len(mark)):
                    if car==mark[i]:
                        pri = int(input("entrer le prix "))
                        d[mark[i]]= pri
                        prix[i]=pri
                        break
                print(d)
                print(prix)
            print("============================ADMIN===============================")
            print("---------------------------BIENVENU-----------------------------")
            print("   mark                                        prix par jour    ")
            print("----------------------------------------------------------------")
            for x,y in d.items():
                print("   ",x,"                                      ",y,"dh")
            print("----------------------------------------------------------------")
            print("================================================================")

    else:
        print("Taper 'user' ou 'admin' ")
        #break
