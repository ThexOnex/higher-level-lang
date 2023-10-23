#reverse a number
num = stock = result = 0
num = int(input("enter number : "))#345

while(num != 0):
    stock = num % 10
    result = result * 10 + stock
    num //= 10

print(result)

#method 2
r = ""
n = 0
n = int(input("enter number : "))

while(n != 0):
    r = r + str(n%10)
    n =n//10

print(r)