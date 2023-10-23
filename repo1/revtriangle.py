#****
#***
#**
#*
#L is num of lines

etl = esp = L = i = j = k = 0
L = int(input("taper L "))
esp = L - 1
etl = 1

while(i < L):
    j = 0
    while(j < etl):#
        print("*", end='')
        j = j + 1
    k =0
    while(k<esp):
        print(" ",end='')
        k = k + 1

    print()
    etl = etl + 1
    esp = esp - 1
    i = i + 1