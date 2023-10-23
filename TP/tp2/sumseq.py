#Calculating the maximum sum of a subsequence:
#Write an algorithm to find the maximum sum of a subsequence in an array of integers

#12389 sum = 17 
#1534 sum = 7


t = [1,2,3,8,9]

taille = add=fin=0
taille= len(t)
j=0

for i in range(taille):
    if t[i] != t[taille-1] and t[i]+1 == t[i+1]:
        add += t[i]
        j=add
    elif t[i] != t[taille-1] and t[i]-1 == t[i-1]:
        add += t[i]
        j=add
        add=0
    elif t[i] == t[taille-1] and t[i]-1 ==t[i-1]:
        add+=t[i]
        j=add
    if fin<j :
        fin=j

print("la somme des plus grande sequence succesive est : ",fin)