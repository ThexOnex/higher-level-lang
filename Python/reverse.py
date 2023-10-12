#reverse a number
num = stock = result = 0
num = int(input("enter number : "))#345

while(num != 0):
    stock = num % 10
    result = result * 10 + stock
    num //= 10

print(result)