from erreur import Erreurnote
try:
    note = 0
    note = float(input("Entrer la note: "))
    if note < 0:
        raise Erreurnote()
    else:
        print(note)
except Exception as E:
    print(E)
# 6 definition
# qcm

# tp/efm
