# Palandrome

def Palandrome(word):
    taille = len(word)
    rev = taille-1

    non = False

    for i in range(int(taille/2)):
        while (rev >= int(rev/2)):
            if word[i] != word[rev]:
                non = True
            rev -= 1
            break

    if non == False:
        print("Ce mot est Palandrome")
    else:
        print("Ce mot n'est pas Palandrome")


Pal = input("Enter le mot ")
Palandrome(Pal)
