# find the two elements in the array that their sum equals 9

def TwoSum(arr, sum):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == sum:
                print(i, "+", j, "=", sum)
                break


TwoSum([1, 3, 5, 6, 11, 23], 9)
