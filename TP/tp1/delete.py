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

print("position est ",pos)

for i in range(pos, taille-1):
    t[i] = t[i+1]

taille-=1
t=t[:taille]
print(t)