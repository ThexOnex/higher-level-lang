taille = 0
t = [1,2,3,4,5,6]
stack = 7
renum = False

for i in range(6):
    if t[i] ==stack:
        renum = True
if renum == True:
    print("Yes")
else:
    print("No")