#   *
#  ***
# *****
#*******


etl = esp = L = i = j = k = 0
L = int(input("taper L "))

esp = L * 2 
etl = 1

while(i<L):
    j = 1
    while(j<esp):
        print(" ",end='')
        #print(" ",end='')
        j+=2
        esp -= 1
    k=0
    while(k<etl):
        print("*", end='')
        k += 1
        #etl -= 1
    if(esp==2):
        esp = 1
    print()
    #esp -= 1
    etl += 2
    i += 1
