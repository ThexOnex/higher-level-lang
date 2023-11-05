# prints the element of an array seperated by comma and space
# except the last element   1, 2, 3, 4, 5

def printarray(str, n):
    str = [0]*n
    for i in range(n):
        str[i] = int(input("fill the array at "))
    for i in str:
        if i != str[n-1]:
            print(i, ", ", end='')
        else:
            print(i)


array = []

printarray(array, 5)
