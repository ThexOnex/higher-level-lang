#can be devised by only himself

t=[61,20,67,17,18,71,73,79,50,97,55,101]
stop = False

for i in range(len(t)):
    j=2
    stop = False
    #half = t[i]/j
    while(j <= t[i]/2 and stop == False):
        if t[i]%j == 0:
            stop = True
        j += 1
    if stop != True:
        print(t[i],"est premier")