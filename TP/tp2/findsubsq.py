# Finding the longest subsequence
# Write an algorithm that finds the longest subsequence of consecutive elements in an array.
t1=[]

t = [1,2,3,6,7,8]
taille=j=stock1=memo=memo2=taille2=0
taille = len(t)

for i in range(taille):
    if t[i] != t[taille-1] and t[i]+1 == t[i+1]:
        if j==0:
            memo = i
        j+=1
    elif(t[i] != t[taille-1] and t[i]-1 == t[i-1]):
        if stock1<=j:
            j+=1
            stock1=j
            memo2=i
        j=0
    elif t[i] == t[taille-1] and t[i]-1 == t[i-1]:
        j+=1
    if stock1<=j:
        stock1=j
        memo2=i

t1 = [0]*stock1
print(stock1," est la taille")

j=0

for i in range(memo,memo2+1):
    t1[j] = t[i]
    j+=1
print("Avant la Recherche : ",t)
print("Apres la Recherche : ",t1)





