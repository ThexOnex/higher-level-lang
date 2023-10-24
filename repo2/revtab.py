t=[4,5,6,7,8,9,10,11,12]#if taille pair the middle stays
temp = taille =half=i= 0
taille = len(t)
print("before : ",t)
j = taille-1
half  = int(taille/2)

while(i<half):
    temp = 0
    while(j!=0):
        temp = t[i]
        t[i] = t[j]
        t[j] = temp
        j-=1
        break
    i+=1
    
print("after :  ",t)