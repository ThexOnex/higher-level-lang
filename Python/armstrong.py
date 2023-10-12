num = num1 = last = n = 0
num = int(input("enter a number : "))#153
num1 = num

while(num1 != 0):
    last = num1 % 10#3 5 1
    print(last)
    num1 = num1 // 10#15 1 
    print(num1)
    n = (last * last * last ) + n#0 = 3 + 30 + 300 + 0 333=5+50+500+333
    print(n) #333 888 

if(n == num):
    print(num,"is an armstong")
else:
    print(num,"is not an armstong")