#   *
#  ***
# *****
#*******




L = int(input("entrer lines"))
esp = etl = 0
etl = 1
esp = L-1

for i in range(L):
    for j in range(esp):
        print(" ",end="")
    for k in range(etl):
        print("*",end="")
    print()
    etl+=2
    esp-=1


