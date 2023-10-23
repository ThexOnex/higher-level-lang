L = j = esp = 0
i = 0
L = int(input("number of lines : "))
esp = L
j = 1

for i in range(L):
    k = esp -1
    for k in range(k,0,-1):#if i didn't write 'k' the triangle 
        print(" ",end='')  #would reverse cuz the range'll say 
                           #that it starts with 0 which is imposible

    print(j * '*')
    j = i + 2
    #i+=1
    esp -=1
