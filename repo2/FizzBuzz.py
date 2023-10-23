n = 0
n = int(input("print the number : "))

for i in range(n):
    if i % 3 == 0:
        if i % 5 ==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)