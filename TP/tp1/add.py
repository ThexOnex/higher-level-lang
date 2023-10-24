taille = 0
t = [1,2,3,4,5]
element = 3
taille=len(t)
pos = 0
print(t)

for i in range(taille):
    if t[i] == element:
        pos = i
        break
    i+=1

print("position est ",pos)#found it
taille+=1#add the lenght
a =[0]*taille

for i in range(taille,pos+1):#change the elements
    t[i] = a[i-1]

print(a)