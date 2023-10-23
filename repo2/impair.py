nbr = taille = 0
t = [1,2,3,4,5,6]
taille = len(t)

for i in range(taille):
    #t[i] = int(input("nbr : "))
    if t[i] % 2 != 0:
        print(t[i]," ",end='')


print("sont des nbr impaire")


