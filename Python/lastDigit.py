#last digit of a num
#greater than 5
# is 0
#less than 6 and greater than 0

n = last = 0
n = int(input("enter a number : "))
last = n % 10
if(last > 5):
    print("last digit of",n,"is",last,"is greater than 5")
elif(last<6 and last != 0):
    print("last digit of",n,"is",last,"less than 6 and greater than 0")
elif(last == 0):
    print("last digit of",n,"is 0")