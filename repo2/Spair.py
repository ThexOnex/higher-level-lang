add = taille = 0

taille = int(input("enter the number of the nbr "))
t = [0] *taille
print(t)
for i in range(taille):
    t[i]=int(input("enter the nbr "))
    if t[i]%2==0:
        add += t[i]

print(t)
print(add,"is the sum of pair numbers")
