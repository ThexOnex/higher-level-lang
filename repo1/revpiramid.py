#*******
# *****
#  ***
#   *


etl = esp = L = i = j = k = 0
L = int(input("taper L "))

etl = L * 2 - 1
esp = 1

while(i<L):
    j = 1
    while(j<esp):
        print(" ",end="")
        j+=1
    k=0
    while(k<etl):
        print("*", end="")
        k += 1
        #etl -= 1
    print()
    esp += 1
    etl -= 2
    i += 1