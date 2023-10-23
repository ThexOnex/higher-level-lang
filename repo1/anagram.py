#An anagram is a condition in which one string or number is rearranged in 
#such a way that each character of the rearranged string or number is 
#part of another string or number. In other words, 
#if the second string is simply a rearrangement of the first,
#it is said to be an anagram of the first.
#listen = silent

array = []
j = S = 0
array = input("string : ")
array2 = input("string 2 : ")

for i in array:
    j +=1
for i in array2:
    S +=1

#print(j)
#print(S)

stock = j
yes = 0

if j == S:
    while(j!=0):
        while(S!=0):
            if array[j-1] == array2[S-1]:
                yes +=1
            S -= 1
        S=stock
        j -= 1

    if yes == stock:
        print("Yes")
    else:
        print("No")

else:
    print("No")
