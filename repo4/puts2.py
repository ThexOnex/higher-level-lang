# write a fct that print every other char in a string 12345678 prints 13579

def puts2(str):
    j = 0
    import sys
    for i in str:
        j += 1
    for i in range(0, j, 2):
        sys.stdout.write(str[i])
    sys.stdout.write("\n")


string = "0123456789"
puts2(string)
