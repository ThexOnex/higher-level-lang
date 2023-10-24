#Given an array of N integers, print the value of all those elements,
#whose indexes form an increasing Arithmetic Progression along with
#the difference in Arithmetic Progression.
#If an element occurs single time then print 0 as difference.


t = [4, 2, 4, 3, 4, 2, 4, 5]
taille =ap=j=0
taille = len(t)
stop = False

stock = 0
print("taille : ",taille)

for i in range(taille):
    stop = False
    j = i+1
    while(stop == False and j<taille):
        if t[i]==stock:#did we work with the number befor?
            i +=1
        if t[i] == t[j]:
            ap = int((j-i))
            stop = True
            again=+1#increment num of both numbers
            t1=[0]*again
            stock = t[j]
            t1[again] = stock #t1 = [t[2],t[2]]
            print(t1)
            print(t[i],"  ",ap)
        if j == taille -1 and stop == False:
            print(t[i],"   0")
        j+=1


