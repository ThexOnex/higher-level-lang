def fact(a):
    for i in range(1, a):
        a *= i
    return a


num = 3
print("Factorielle de ce nombre est ", fact(num))
