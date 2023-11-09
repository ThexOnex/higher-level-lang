
def plusGrand(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return a, b


x = 20
y = 30
print("la plus grande nombre est ", plusGrand(x, y))
# 3
c = 40
print(plusGrand(c, plusGrand(x, y)))
# 4
d = 50
print(plusGrand(plusGrand(x, y), plusGrand(c, d)))
# 5
e = 60
print(plusGrand(e, plusGrand(x, y), plusGrand(c, d)))
