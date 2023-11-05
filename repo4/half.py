# write a fct that prints the second half of a string followed by a new line
# without print
def half(str):
    j = 0
    import sys
    for i in str:
        j += 1
    for i in range(int(j/2), j):
        sys.stdout.write(str[i])
    sys.stdout.write("\n")


string = "this string"
half(string)
