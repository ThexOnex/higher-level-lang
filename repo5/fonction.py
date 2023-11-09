# creation
# dans presedure on note print m dans fonction return m
def moy(note1, note2):
    s = 0
    m = 0
    s = note1 + note2
    m = s/2
    return m

# appel
x = 0
y = 0
x = float(input("Entrer la 1er note "))
y = float(input("Entrer la 2eme note "))

print(moy(x, y))
r = 0
r = moy(x, y)
if r >= 10:
    print("admin")
else:
    print("redoublent")
