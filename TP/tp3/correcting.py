mark=['Dacia','Audi','Ford']
prix=[400,250,250]
bol = False
d={'mark':mark,'prix':prix}


while(bol==False):
    mark1 = input("Entrer la mark ")
    for i in range(len(mark)):
        if mark1==mark[i]:
            print("le prix est",prix[i])
            bol=True
            break
        elif i == len(mark)-1:
            bol=False
        else:
            continue
    if bol==False:
        print("on n'a pas trouve la mark")
