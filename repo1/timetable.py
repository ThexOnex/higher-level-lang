#time table of the number and the other number after it till it reachs 10

i = num = S = j = 0
num = int(input("Enter the nbr "))
 
#j = num
for j in range(num,10):
    for i in range(1,11):
        S = num * i # 1 * 5 = 5 1+...10
        print(num,"*",i,"=",S)
    print()
    #j +=1
    num +=1


