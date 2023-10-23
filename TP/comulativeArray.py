#Cumulative sum

#Write an algorithm that creates a new array where each element is the cumulative sum of the elements of the original array.
#For example, [1, 2, 3, 4] should become [1, 3, 6, 10]

t = [1,2,3,4,5,6,7]
taille =add = 0
taille = len(t)
print(t)
add = t[0]
for i in range(1,taille):
    add += t[i]
    t[i] = add

print(t)