# sum a 2d list
twod = [[1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1]]


def sum2d(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            sum += arr[i][j]
    return sum


sum = 0
sum = sum2d(twod)
print(sum)
