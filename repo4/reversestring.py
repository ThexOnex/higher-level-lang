# fct that reverse a string

def reverse(str):
    j = 0
    for i in str:
        j += 1
    for k in range(j-1, -1, -1):
        print(str[k], end='')


string = "bla bla bla"
reverse(string)
