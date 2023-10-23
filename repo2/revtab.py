t=[4,5,6,7,8,9,10,11,12]#if taille pair the middle stays
temp = taille =m=half=i= 0
taille = len(t)
print("before : ",t)
j = taille-1
half  = int(taille/2)

while(i<taille and m<half):
    temp = 0
    stop = False
    while(j!=0 and stop == False):
        temp = t[i]
        t[i] = t[j]
        t[j] = temp
        stop = True
        j-=1
    i+=1
    m+=1

print("after :  ",t)