# sort only the premiest numbers in the array

array = [1, 2, 11, 22, 13, 99, 7]
temp = premier = 0
stock = 0
arrP = []
taille = 0


def IsPremier(num):  # is it a premier number?
    if num == 1:
        return -1
    for i in range(2, int(num/2)):
        if num % i == 0:
            return -1
    return 0


for i in range(len(array)):
    premier = IsPremier(array[i])
    if premier == -1:
        continue
    for j in range(i+1, len(array)):
        premier = IsPremier(array[i])
        if premier == -1:
            continue
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(array)
