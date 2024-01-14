def ecrire():
    txt = ""
    f = open("C://test2.txt", "a")
    ph = input("Taper votre phrase ")
    txt = "\n" + ph
    f.write(txt)
    f.close()


ecrire()
f1 = open("C://test2.txt", "r")
print(f1.readline())
