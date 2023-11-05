def password():
    passe = ""
    shif = "1234567890"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bolTaille = bolUpper = bolShif = bolSpecial = stop = False
    special = ['!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']

    while (stop == False):
        passe = input("Entrer le mode de passe: ")
        taille = len(passe)
        # 8 or more
        if taille >= 8:
            bolTaille = True
        else:
            print("Entrer 8 characteres ou plus")
            print("faible mode de passe")
            continue
        # check for uppercase
        for i in range(taille):
            for j in range(len(upper)):
                if passe[i] == upper[j]:
                    bolUpper = True
                    break
        if bolUpper != True:
            print("Entrer une charactere Majuscule ou plus")
            print("faible mode de passe")
            continue
        # check for numbers
        for i in range(taille):
            for j in range(len(shif)):
                if passe[i] == shif[j]:
                    bolShif = True
                    break
        if bolShif != True:
            print("Entrer un nombre ou plus")
            print("faible mode de passe")
            continue
        # check special char
        for i in range(taille):
            for j in range(len(special)):
                if passe[i] == special[j]:
                    bolSpecial = True
                    break
        if bolSpecial != True:
            print("Entrer une charactere special ou plus")
            print("faible mode de passe")
            continue
        break

    print("Mode de passe Fort")


password()
