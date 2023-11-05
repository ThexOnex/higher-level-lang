# convert a string into an integer
# take into acc -

def _atoi(strn):
    numbers = "123456789"
    output = ""
    word = sign = False
    for i in range(len(strn)):
        if strn[i] == '-':
            for j in range(len(numbers)):
                if strn[i+1] == numbers[j]:
                    sign = True
                    break
            if sign != False:
                output += '-'
        for j in numbers:
            if strn[i] == j:
                output += j
                word = True
                break
    if word == True:
        number = int(output)
        return number
    else:
        return 0


num = 0
num = _atoi("2sef44eseg35dg5")
print(num)
num = _atoi("45")
print(num)
num = _atoi("fdhhdh")
print(num)
num = _atoi("--++++++------++++-23")
print(num)
num = _atoi("2se=dg5")
print(num)
num = _atoi("0")
print(num)
num = _atoi("suite 536")
print(num)
num = _atoi("-    =    +  +   -    -  45345- 4345- ")
print(num)
