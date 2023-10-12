money = bank = rest = 0
fin = stop = False

while(stop == False):
    money = int(input("enter 3 DH : "))
    while((money == 1 or money == 2 or money ==5) and fin == False):
        bank = money + bank #1 , 
        if(bank >= 3):
            rest = bank - 3 # 5 - 3 = 2 dh
            fin = True
        if(bank < 3):# 1
            money = int(input("not enough, enter more : "))#2
            #money = money + bank#2 + 1
    if(fin != False):
        stop = True
        print("here's your order , rest is", rest ,"DH")
    else:
        print("please enter only 1 dh, 2dh and 5dh")