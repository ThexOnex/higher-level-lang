# Mot = ""
# Mot = input("taper un mot ")

# for i in range(len(Mot)):
#     print(Mot[i])

Mot = "Bonsoir"
nm = ""


for i in range(len(Mot)):
    if Mot[i] == 'o':
        nm += '*'
    else:
        nm += Mot[i]

print(nm)