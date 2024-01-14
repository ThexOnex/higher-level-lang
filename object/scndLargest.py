# Find the second largest number in a given array
second = 0
array = [20, 4, 3, 2, 33]


def find2ND(arr):
    stock = arr[0]
    for i in range(len(arr)):
        if arr[i] > stock:
            stock = arr[i]
        if arr[i] != stock:
            stock2 = arr[i]

    for i in range(len(arr)):
        if arr[i] > stock2 and arr[i] != stock:
            stock2 = arr[i]

    return stock2


second = find2ND(array)
print("second largest number in the array is: ", second)
print(array[-2])
array.append
