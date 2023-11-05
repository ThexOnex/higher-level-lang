# write a function that returns the lenght of a string

def _len(str):
    j = 0
    for i in str:
        j += 1
    print("the lenght of the string is", j)


theString = "blablabla"
_len(theString)
