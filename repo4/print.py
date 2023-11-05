# write a fct that prints a string without using print fct and it should end with a new line

def _print(str):
    import sys
    for i in str:
        sys.stdout.write(i)
    sys.stdout.write("\n")


string = "bla bla bla"

_print(string)

print("new line ?")
