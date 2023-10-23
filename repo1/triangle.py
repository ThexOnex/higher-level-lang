#   *
#  **
# ***
#****

etl = esp = L = i = j = k = 0
L = int(input("taper L "))

etl = 1
esp = L-1

for i in range(L):
    j = 0
    for j in range(esp):
        print(" ",end='')
    k = 0
    for k in range(etl):
        print("*", end='')
    print()
    esp -= 1
    etl += 1